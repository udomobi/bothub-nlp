import json
from tempfile import mkdtemp
from collections import defaultdict

from rasa_nlu.model import Trainer
from rasa_nlu.training_data import Message, TrainingData
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.training_data.formats.readerwriter import TrainingDataWriter
from rasa_nlu.utils import json_to_string

from .utils import get_rasa_nlu_config_from_update
from .utils import PokeLogging
from .utils import backend
from .persistor import BothubPersistor
from . import logger


class BothubWriter(TrainingDataWriter):
    def dumps(self, training_data, **kwargs):
        js_entity_synonyms = defaultdict(list)
        for k, v in training_data.entity_synonyms.items():
            if k != v:
                js_entity_synonyms[v].append(k)

        formatted_synonyms = [
            {"value": value, "synonyms": syns}
            for value, syns in js_entity_synonyms.items()
        ]

        formatted_examples = [
            example.as_dict() for example in training_data.training_examples
        ]
        formatted_label_examples = [
            example.as_dict() for example in training_data.label_training_examples or []
        ]

        return json_to_string(
            {
                "rasa_nlu_data": {
                    "common_examples": formatted_examples,
                    "label_examples": formatted_label_examples,
                    "regex_features": training_data.regex_features,
                    "entity_synonyms": formatted_synonyms,
                }
            },
            **kwargs
        )


class BothubTrainingData(TrainingData):
    def __init__(self, label_training_examples=None, **kwargs):
        if label_training_examples:
            self.label_training_examples = self.sanitize_examples(
                label_training_examples
            )
        else:
            self.label_training_examples = []
        super().__init__(**kwargs)

    def as_json(self, **kwargs):
        return BothubWriter().dumps(self)


def train_update(update, by, repository_authorization):
    update_request = backend().request_backend_start_training_nlu(
        update, by, repository_authorization
    )
    with PokeLogging() as pl:
        try:
            examples = []
            label_examples = []

            get_examples = backend().request_backend_get_entities_and_labels_nlu(
                update,
                update_request.get("language"),
                json.dumps(update_request),
                repository_authorization,
            )

            for example in get_examples.get('examples'):
                examples.append(
                    Message.build(
                        text=example.get('text'),
                        intent=example.get("intent"),
                        entities=example.get('entities'),
                    )
                )

            for label_example in get_examples.get("label_examples"):
                label_examples.append(
                    Message.build(
                        text=label_example.get('text'),
                        entities=label_example.get('entities'),
                    )
                )

            rasa_nlu_config = get_rasa_nlu_config_from_update(update_request)
            trainer = Trainer(rasa_nlu_config, ComponentBuilder(use_cache=False))
            training_data = BothubTrainingData(
                label_training_examples=label_examples, training_examples=examples
            )

            trainer.train(training_data)

            persistor = BothubPersistor(update, repository_authorization)
            trainer.persist(
                mkdtemp(),
                persistor=persistor,
                project_name=str(update_request.get("repository_uuid")),
                fixed_model_name=str(update_request.get("update_id")),
            )
        except Exception as e:
            logger.exception(e)
            backend().request_backend_trainfail_nlu(update, repository_authorization)
            raise e
        finally:
            backend().request_backend_traininglog_nlu(
                update, pl.getvalue(), repository_authorization
            )
