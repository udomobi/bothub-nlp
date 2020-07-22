import unittest
import uuid
from unittest.mock import patch

from celery_app import train_update



class TestTrainTask(unittest.TestCase):

    bert_language = "pt_br"
    # bert_language = "en"

    def setUp(self, *args):

        self.repository_authorization = uuid.uuid4()
        self.current_update = {
            "ready_for_train": True,
            "current_version_id": 6647,
            "repository_authorization_user_id": 303
        }

    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_save_queue_id",
        return_value={},
    )

    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_start_training_nlu",
        return_value={
            "language": bert_language,
            "repository_version": 6647,
            "repository_uuid": "e1e8a0fa-625c-4ba3-8b91-4c9f308db791",
            "intent": [],
            "total_training_end": 4,
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": False
        },
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_get_examples",
        return_value={
            "count": 358,
            "next": None,
            "previous": None,
            "results": [
                {"text": "ss", "intent": "affirmative", "entities": []},
                {"text": "okay", "intent": "affirmative", "entities": []},
                {"text": "afirmativo", "intent": "affirmative", "entities": []},
                {"text": "okk", "intent": "affirmative", "entities": []},
                {"text": "okayy", "intent": "affirmative", "entities": []},
                {"text": "certo", "intent": "affirmative", "entities": []},
                {"text": "nops", "intent": "negative", "entities": []},
                {"text": "no", "intent": "negative", "entities": []},
                {"text": "nope", "intent": "negative", "entities": []},
                {"text": "não sei", "intent": "doubt", "entities": []},
                {"text": "naa", "intent": "negative", "entities": []},
                {"text": "na", "intent": "negative", "entities": []},
                {"text": "não", "intent": "negative", "entities": []},
                {"text": "talvez nao", "intent": "negative", "entities": []},
                {"text": "nnn", "intent": "negative", "entities": []},
                {"text": "nn", "intent": "negative", "entities": []},
                {"text": "isso", "intent": "affirmative", "entities": []},
                {"text": "sim, preciso daquilo", "intent": "affirmative", "entities": []},
                {"text": "sim, desejo isso", "intent": "affirmative", "entities": []},
                {"text": "sim, quero isso", "intent": "affirmative", "entities": []},
                {"text": "não ne", "intent": "negative", "entities": []},
                {"text": "tenho que pensar", "intent": "doubt", "entities": []},
                {"text": "talvez", "intent": "doubt", "entities": []},
                {"text": "é", "intent": "affirmative", "entities": []},
                {"text": "quero", "intent": "affirmative", "entities": []},
                {"text": "quero sim", "intent": "affirmative", "entities": []},
                {"text": "negativo", "intent": "negative", "entities": []},
                {"text": "siim", "intent": "affirmative", "entities": []},
                {"text": "boa sim", "intent": "affirmative", "entities": []},
                # {"text": "ótima ideia", "intent": "affirmative", "entities": []},
                # {"text": "já to", "intent": "affirmative", "entities": []},
                # {"text": "nop", "intent": "negative", "entities": []},
                # {"text": "aham aham", "intent": "affirmative", "entities": []},
                # {"text": "já namorei", "intent": "affirmative", "entities": []},
                # {"text": "docs", "intent": "bias", "entities": []},
                # {"text": "sac digital", "intent": "bias", "entities": []},
                # {"text": "sac", "intent": "bias", "entities": []},
                # {"text": "eja", "intent": "bias", "entities": []},
                # {"text": "simn", "intent": "affirmative", "entities": []},
                # {"text": "sinm", "intent": "affirmative", "entities": []},
                # {"text": "matricula", "intent": "bias", "entities": []},
                # {"text": "matrícula", "intent": "bias", "entities": []},
                # {"text": "terceiros", "intent": "bias", "entities": []},
                # {"text": "empreendimentos", "intent": "bias", "entities": []},
                # {"text": "pode pá", "intent": "affirmative", "entities": []},
                # {"text": "porra", "intent": "bias", "entities": []},
                # {"text": "vamos", "intent": "affirmative", "entities": []},
                # {"text": "pode ser", "intent": "affirmative", "entities": []},
                # {"text": "hoje estou num relacionamento abusivo", "intent": "bias", "entities": []},
                # {"text": "sim, gostei disso", "intent": "affirmative", "entities": []},
                # {"text": "sim, gostei da ideia", "intent": "affirmative", "entities": []},
                # {"text": "conta comigo", "intent": "affirmative", "entities": []},
                # {"text": "funcionou não", "intent": "negative", "entities": []},
                # {"text": "seria legal se fossemos", "intent": "affirmative", "entities": []},
                # {"text": "não tenho email", "intent": "negative", "entities": []},
                # {"text": "n gosto disso", "intent": "negative", "entities": []},
                # {"text": "nem queria dizer isso", "intent": "negative", "entities": []},
                # {"text": "para com isso, não pode", "intent": "negative", "entities": []},
                # {"text": "melhor nao falar nada", "intent": "negative", "entities": []},
                # {"text": "nem deve ser tão bom assim", "intent": "negative", "entities": []},
                # {"text": "não queria ter que dizer isso", "intent": "negative", "entities": []},
                # {"text": "deixa para lá", "intent": "negative", "entities": []},
                # {"text": "não queria ter que dizer isso", "intent": "negative", "entities": []},
                # {"text": "deixa para lá", "intent": "negative", "entities": []},
                # {"text": "sem condições", "intent": "negative", "entities": []},
                # {"text": "nem pensar", "intent": "negative", "entities": []},
                # {"text": "estou mau", "intent": "negative", "entities": []},
                # {"text": "estou", "intent": "affirmative", "entities": []},
                # {"text": "consigu", "intent": "affirmative", "entities": []},
                # {"text": "consigo sin", "intent": "affirmative", "entities": []},
                # {"text": "não consigo", "intent": "negative", "entities": []},
                # {"text": "consigo", "intent": "affirmative", "entities": []},
                # {"text": "fazer cancelamento", "intent": "negative", "entities": []},
                # {"text": "cancelamento", "intent": "negative", "entities": []},
                # {"text": "nao tenho", "intent": "negative", "entities": []},
                # {"text": "pior que nao", "intent": "negative", "entities": []},
                # {"text": "pior que não", "intent": "negative", "entities": []},
                # {"text": "nem tenho", "intent": "negative", "entities": []},
                # {"text": "não tenho", "intent": "negative", "entities": []},
                # {"text": "pode po", "intent": "affirmative", "entities": []},
                # {"text": "dentaria", "intent": "bias", "entities": []},
                # {"text": "coroa", "intent": "bias", "entities": []},
                # {"text": "também estou", "intent": "affirmative", "entities": []},
                # {"text": "não quero", "intent": "negative", "entities": []},
                # {"text": "não estou", "intent": "negative", "entities": []},
                # {"text": "coroa dentaria", "intent": "bias", "entities": []},
                # {"text": "sei la mano", "intent": "doubt", "entities": []},
                # {"text": "inclui ceromero?", "intent": "bias", "entities": []},
                # {"text": "buco maxilar", "intent": "bias", "entities": []},
                # {"text": "o plano inclui", "intent": "bias", "entities": []},
                # {"text": "buco", "intent": "bias", "entities": []},
                # {"text": "belezaaaaa", "intent": "affirmative", "entities": []},
                # {"text": "eu também", "intent": "affirmative", "entities": []},
                # {"text": "não, como faço?", "intent": "negative", "entities": []},
                # {"text": "pior que nunca", "intent": "negative", "entities": []},
                # {"text": "varias vezes", "intent": "affirmative", "entities": []},
                # {"text": "um pouco", "intent": "affirmative", "entities": []},
                # {"text": "prometoo", "intent": "affirmative", "entities": []},
                # {"text": "acho que faço isso", "intent": "doubt", "entities": []},
                # {"text": "Não estou bem", "intent": "negative", "entities": []},
                # {"text": "já mas", "intent": "affirmative", "entities": []},
                # {"text": "ja", "intent": "affirmative", "entities": []},
                # {"text": "Não estou bem hoje", "intent": "negative", "entities": []},
                # {"text": "por favor", "intent": "affirmative", "entities": []},
                # {"text": "não quero mais isso", "intent": "negative", "entities": []},
                # {"text": "não estou feliz", "intent": "negative", "entities": []},
                # {"text": "não estou namorando", "intent": "negative", "entities": []},
                # {"text": "a ta sei", "intent": "affirmative", "entities": []},
                # {"text": "tenho com certeza", "intent": "affirmative", "entities": []},
                # {"text": "tenho concerteza", "intent": "affirmative", "entities": []},
                # {"text": "tenho sim", "intent": "affirmative", "entities": []},
                # {"text": "tenho agora", "intent": "affirmative", "entities": []},
                # {"text": "não, isso é demais pra mim", "intent": "negative", "entities": []},
                # {"text": "não, como podemos proceder?", "intent": "negative", "entities": []},
                # {"text": "to namorando sim", "intent": "affirmative", "entities": []},
                # {"text": "too namorando", "intent": "affirmative", "entities": []},
                # {"text": "que otimo", "intent": "affirmative", "entities": []},
                # {"text": "otimo", "intent": "affirmative", "entities": []},
                # {"text": "nada horrivel", "intent": "negative", "entities": []},
                # {"text": "horrivel demais", "intent": "negative", "entities": []},
                # {"text": "estou em um lugar como esse", "intent": "affirmative", "entities": []},
                # {"text": "estou já", "intent": "affirmative", "entities": []},
                # {"text": "já estou", "intent": "affirmative", "entities": []},
                # {"text": "tudo", "intent": "affirmative", "entities": []},
                # {"text": "mais ou menos, porque?", "intent": "doubt", "entities": []},
                # {"text": "mais ou menos, pq?", "intent": "doubt", "entities": []},
                # {"text": "já mas não foi muito bom", "intent": "affirmative", "entities": []},
                # {"text": "eu também estou", "intent": "affirmative", "entities": []},
                # {"text": "tou namorando", "intent": "affirmative", "entities": []},
                # {"text": "nunca passei", "intent": "negative", "entities": []},
                # {"text": "mas não foi muito bom", "intent": "doubt", "entities": []},
                # {"text": "tudo uma merda", "intent": "negative", "entities": []},
                # {"text": "tudo pessimo", "intent": "negative", "entities": []},
                # {"text": "tudo horrivel", "intent": "negative", "entities": []},
                # {"text": "tudo horrível", "intent": "negative", "entities": []},
                # {"text": "pessimo", "intent": "negative", "entities": []},
                # {"text": "horrivel", "intent": "negative", "entities": []},
                # {"text": "uma merda", "intent": "negative", "entities": []},
                # {"text": "namoro", "intent": "affirmative", "entities": []},
                # {"text": "fui estrupada", "intent": "bias", "entities": []},
                # {"text": "quero morrer agora", "intent": "bias", "entities": []},
                # {"text": "mas minha amiga esta sofrendo com abuso. O namorado dela grita com ele", "intent": "bias", "entities": []},
                # {"text": "estou bem", "intent": "affirmative", "entities": []},
                # {"text": "meu namorado esta me batendo", "intent": "bias", "entities": []},
                # {"text": "também relacionamento abusivo", "intent": "bias", "entities": []},
                # {"text": "ja", "intent": "affirmative", "entities": []},
                # {"text": "já", "intent": "affirmative", "entities": []},
                # {"text": "minha familia me apoia", "intent": "bias", "entities": []},
                # {"text": "estou em um relacionamento abusivo", "intent": "bias", "entities": []},
                # {"text": "estou sendo estrupada", "intent": "bias", "entities": []},
                # {"text": "anham", "intent": "affirmative", "entities": []},
                # {"text": "sim estou namorando", "intent": "affirmative", "entities": []},
                # {"text": "estou namorando", "intent": "affirmative", "entities": []},
                # {"text": "sim unhum", "intent": "affirmative", "entities": []},
                # {"text": "ahan", "intent": "affirmative", "entities": []},
                # {"text": "aham", "intent": "affirmative", "entities": []},
                # {"text": "minha família", "intent": "bias", "entities": []},
                # {"text": "minha familia", "intent": "bias", "entities": []},
                # {"text": "relacionamento", "intent": "bias", "entities": []},
                # {"text": "relacionamento abusivo", "intent": "bias", "entities": []},
                # {"text": "nunca por isso", "intent": "negative", "entities": []},
                # {"text": "umhum claro", "intent": "affirmative", "entities": []},
                # {"text": "estou fincando", "intent": "affirmative", "entities": []},
                # {"text": "as vezes", "intent": "doubt", "entities": []},
                # {"text": "umhum", "intent": "affirmative", "entities": []},
                # {"text": "abuso emocional", "intent": "bias", "entities": []},
                # {"text": "não me apoia", "intent": "negative", "entities": []},
                # {"text": "estou namorando..", "intent": "affirmative", "entities": []},
                # {"text": "to naum... mas ja namorei um porquinho?", "intent": "negative", "entities": []},
                # {"text": "to naum... mas nunca se sabe", "intent": "doubt", "entities": []},
                # {"text": "to naum...", "intent": "negative", "entities": []},
                # {"text": "to naum", "intent": "negative", "entities": []},
                # {"text": "to namorando", "intent": "affirmative", "entities": []},
                # {"text": "pior que já", "intent": "affirmative", "entities": []},
                # {"text": "pior que ja", "intent": "affirmative", "entities": []},
                # {"text": "entendi", "intent": "affirmative", "entities": []},
                # {"text": "não entendi", "intent": "doubt", "entities": []},
                # {"text": "acho que uma amiga", "intent": "doubt", "entities": []},
                # {"text": "acho que com uma amiga minha", "intent": "doubt", "entities": []},
                # {"text": "não ne!! estou apanhando demais", "intent": "negative", "entities": []},
                # {"text": "naum", "intent": "negative", "entities": []},
                # {"text": "naum neh", "intent": "negative", "entities": []},
                # {"text": "não né", "intent": "negative", "entities": []},
                # {"text": "morte", "intent": "bias", "entities": []},
                # {"text": "morrer", "intent": "bias", "entities": []},
                # {"text": "futebol", "intent": "bias", "entities": []},
                # {"text": "gosto de futebol", "intent": "bias", "entities": []},
                # {"text": "meu namorou bateu na minha cara", "intent": "bias", "entities": []},
                # {"text": "não ne!!", "intent": "negative", "entities": []},
                # {"text": "preciso de ajuda", "intent": "bias", "entities": []},
                # {"text": "me", "intent": "bias", "entities": []},
                # {"text": "agride", "intent": "bias", "entities": []},
                # {"text": "agrediu", "intent": "bias", "entities": []},
                # {"text": "tenho", "intent": "affirmative", "entities": []},
                # {"text": "mais ou menos", "intent": "doubt", "entities": []},
                # {"text": "me bateu", "intent": "bias", "entities": []},
                # {"text": "estuprada", "intent": "bias", "entities": []},
                # {"text": "sim, tou namorando", "intent": "affirmative", "entities": []},
                # {"text": "errado", "intent": "negative", "entities": []},
                # {"text": "oi", "intent": "bias", "entities": []},
                # {"text": "ola", "intent": "bias", "entities": []},
                # {"text": "e apois", "intent": "affirmative", "entities": []},
                # {"text": "desejo", "intent": "affirmative", "entities": []},
                # {"text": "claro que sim", "intent": "affirmative", "entities": []},
                # {"text": "nõa", "intent": "negative", "entities": []},
                # {"text": "nã", "intent": "negative", "entities": []},
                # {"text": "pode com força", "intent": "affirmative", "entities": []},
                # {"text": "claro, pode com certeza", "intent": "affirmative", "entities": []},
                # {"text": "com certeza", "intent": "affirmative", "entities": []},
                # {"text": "quero não, cancele", "intent": "negative", "entities": []},
                # {"text": "cancelar", "intent": "negative", "entities": []},
                # {"text": "posso sim", "intent": "affirmative", "entities": []},
                # {"text": "pode me enviar sim, por favor", "intent": "affirmative", "entities": []},
                # {"text": "aceito sim", "intent": "affirmative", "entities": []},
                # {"text": "afirmativo, pode me mandar sim!", "intent": "affirmative", "entities": []},
                # {"text": "sim estou disponível", "intent": "affirmative", "entities": []},
                # {"text": "quero me mande por favor", "intent": "affirmative", "entities": []},
                # {"text": "acredito", "intent": "affirmative", "entities": []},
                # {"text": "conheço", "intent": "affirmative", "entities": []},
                # {"text": "verdade", "intent": "affirmative", "entities": []},
                # {"text": "vdd", "intent": "affirmative", "entities": []},
                # {"text": "positivo", "intent": "affirmative", "entities": []},
                # {"text": "uhum", "intent": "affirmative", "entities": []},
                # {"text": "acredito que nao", "intent": "doubt", "entities": []},
                # {"text": "acredito q sim", "intent": "doubt", "entities": []},
                # {"text": "creio que não", "intent": "doubt", "entities": []},
                # {"text": "creio que sim!", "intent": "doubt", "entities": []},
                # {"text": "creio q s", "intent": "doubt", "entities": []},
                # {"text": "nem sei", "intent": "doubt", "entities": []},
                # {"text": "sei n viu", "intent": "doubt", "entities": []},
                # {"text": "acho que não", "intent": "negative", "entities": []},
                # {"text": "acho q n", "intent": "negative", "entities": []},
                # {"text": "acho q s", "intent": "doubt", "entities": []},
                # {"text": "acho que sim", "intent": "doubt", "entities": []},
                # {"text": "assim mesmo", "intent": "affirmative", "entities": []},
                # {"text": "pode crer", "intent": "affirmative", "entities": []},
                # {"text": "claro que sim", "intent": "affirmative", "entities": []},
                # {"text": "exatoo", "intent": "affirmative", "entities": []},
                # {"text": "exatamente!", "intent": "affirmative", "entities": []},
                # {"text": "issoo", "intent": "affirmative", "entities": []},
                # {"text": "ehh", "intent": "affirmative", "entities": []},
                # {"text": "to raciocinando sobre isso", "intent": "doubt", "entities": []},
                # {"text": "estou raciocinando", "intent": "doubt", "entities": []},
                # {"text": "preciso pensar", "intent": "doubt", "entities": []},
                # {"text": "to pensando", "intent": "doubt", "entities": []},
                # {"text": "n to certa disso", "intent": "doubt", "entities": []},
                # {"text": "n to tao segura", "intent": "doubt", "entities": []},
                # {"text": "pode ser que sim, pode ser que não", "intent": "doubt", "entities": []},
                # {"text": "é, pode ser", "intent": "affirmative", "entities": []},
                # {"text": "nem a pau", "intent": "negative", "entities": []},
                # {"text": "nem que a vaca tussa", "intent": "negative", "entities": []},
                # {"text": "nem", "intent": "negative", "entities": []},
                # {"text": "noo", "intent": "negative", "entities": []},
                # {"text": "non", "intent": "negative", "entities": []},
                # {"text": "nonono", "intent": "negative", "entities": []},
                # {"text": "no way", "intent": "negative", "entities": []},
                # {"text": "de jeito maneira", "intent": "negative", "entities": []},
                # {"text": "n n", "intent": "negative", "entities": []},
                # {"text": "nnnn", "intent": "negative", "entities": []},
                # {"text": "quero n", "intent": "negative", "entities": []},
                # {"text": "deus me livre", "intent": "negative", "entities": []},
                # {"text": "de forma alguma", "intent": "negative", "entities": []},
                # {"text": "de jeito nenhum", "intent": "negative", "entities": []},
                # {"text": "naam", "intent": "negative", "entities": []},
                # {"text": "num sei", "intent": "doubt", "entities": []},
                # {"text": "afirmativo!", "intent": "affirmative", "entities": []},
                # {"text": "evidente que não", "intent": "negative", "entities": []},
                # {"text": "obviamente", "intent": "affirmative", "entities": []},
                # {"text": "evidente", "intent": "affirmative", "entities": []},
                # {"text": "certamente", "intent": "affirmative", "entities": []},
                # {"text": "ctz q sim", "intent": "affirmative", "entities": []},
                # {"text": "ctz", "intent": "affirmative", "entities": []},
                # {"text": "tenho ctz", "intent": "affirmative", "entities": []},
                # {"text": "n to segura", "intent": "doubt", "entities": []},
                # {"text": "não estou seguro", "intent": "doubt", "entities": []},
                # {"text": "hmm, n sei", "intent": "doubt", "entities": []},
                # {"text": "tenho minhas dúvidas", "intent": "doubt", "entities": []},
                # {"text": "tô na dúvida", "intent": "doubt", "entities": []},
                # {"text": "sei n", "intent": "doubt", "entities": []},
                # {"text": "jamais", "intent": "negative", "entities": []},
                # {"text": "nunca", "intent": "negative", "entities": []},
                # {"text": "sempre", "intent": "affirmative", "entities": []},
                # {"text": "evidente", "intent": "affirmative", "entities": []},
                # {"text": "smm", "intent": "affirmative", "entities": []},
                # {"text": "s", "intent": "affirmative", "entities": []},
                # {"text": "obvio que sim", "intent": "affirmative", "entities": []},
                # {"text": "é óbvio!", "intent": "affirmative", "entities": []},
                # {"text": "mas é claro", "intent": "affirmative", "entities": []},
                # {"text": "óbvio", "intent": "affirmative", "entities": []},
                # {"text": "eh", "intent": "affirmative", "entities": []},
                # {"text": "nao", "intent": "negative", "entities": []},
                # {"text": "claro que não", "intent": "negative", "entities": []},
                # {"text": "não mesmo", "intent": "negative", "entities": []},
                # {"text": "nam", "intent": "negative", "entities": []},
                # {"text": "quero não", "intent": "negative", "entities": []},
                # {"text": "tranquilo", "intent": "affirmative", "entities": []},
                # {"text": "isso aí", "intent": "affirmative", "entities": []},
                # {"text": "isso mesmo", "intent": "affirmative", "entities": []},
                # {"text": "tá massa!", "intent": "affirmative", "entities": []},
                # {"text": "certinho", "intent": "affirmative", "entities": []},
                # {"text": "ta beleza", "intent": "affirmative", "entities": []},
                # {"text": "tudo bem, então", "intent": "affirmative", "entities": []},
                # {"text": "tudo bem", "intent": "affirmative", "entities": []},
                # {"text": "unhum", "intent": "affirmative", "entities": []},
                # {"text": "entendo", "intent": "affirmative", "entities": []},
                # {"text": "tendi", "intent": "affirmative", "entities": []},
                # {"text": "beleza!", "intent": "affirmative", "entities": []},
                # {"text": "tá certo", "intent": "affirmative", "entities": []},
                # {"text": "tá ok", "intent": "affirmative", "entities": []},
                # {"text": "ok", "intent": "affirmative", "entities": []},
                # {"text": "certo", "intent": "affirmative", "entities": []},
                # {"text": "eu não tenho certeza", "intent": "doubt", "entities": []},
                # {"text": "não tenho certeza", "intent": "doubt", "entities": []},
                # {"text": "não sei", "intent": "doubt", "entities": []},
                # {"text": "eu não sei", "intent": "doubt", "entities": []},
                # {"text": "certeza!", "intent": "affirmative", "entities": []},
                # {"text": "com certeza", "intent": "affirmative", "entities": []},
                # {"text": "talvez sim", "intent": "doubt", "entities": []},
                # {"text": "não gostaria", "intent": "negative", "entities": []},
                # {"text": "eu não gostaria", "intent": "negative", "entities": []},
                # {"text": "gostaria", "intent": "affirmative", "entities": []},
                # {"text": "eu gostaria", "intent": "affirmative", "entities": []},
                # {"text": "não, não faço", "intent": "negative", "entities": []},
                # {"text": "sim, eu faço", "intent": "affirmative", "entities": []},
                # {"text": "não posso fazer isso", "intent": "negative", "entities": []},
                # {"text": "posso fazer isso", "intent": "affirmative", "entities": []},
                # {"text": "eu não posso", "intent": "negative", "entities": []},
                # {"text": "não posso", "intent": "negative", "entities": []},
                # {"text": "não, eu não sou", "intent": "negative", "entities": []},
                # {"text": "sim, eu sou", "intent": "affirmative", "entities": []},
                # {"text": "to dentro", "intent": "affirmative", "entities": []},
                # {"text": "não sou", "intent": "negative", "entities": []},
                # {"text": "eu realmente quero", "intent": "affirmative", "entities": []},
                # {"text": "eu quero isso", "intent": "affirmative", "entities": []},
                # {"text": "não quero", "intent": "negative", "entities": []},
                # {"text": "eu quero", "intent": "affirmative", "entities": []},
                # {"text": "sim", "intent": "affirmative", "entities": []},
                # {"text": "quero", "intent": "affirmative", "entities": []},
                # {"text": "n quero", "intent": "negative", "entities": []},
                # {"text": "não é", "intent": "negative", "entities": []},
                # {"text": "não é", "intent": "negative", "entities": []},
                # {"text": "não é", "intent": "negative", "entities": []},
                # {"text": "é", "intent": "affirmative", "entities": []},
                # {"text": "eu não quero", "intent": "negative", "entities": []},
                # {"text": "eu realmente quero", "intent": "affirmative", "entities": []},
                # {"text": "não", "intent": "negative", "entities": []},
                # {"text": "talvez não", "intent": "doubt", "entities": []},
                # {"text": "talvez sim", "intent": "doubt", "entities": []},
                # {"text": "eu quero sim", "intent": "affirmative", "entities": []},
                # {"text": "talvez", "intent": "doubt", "entities": []},
                # {"text": "talvez", "intent": "doubt", "entities": []},
                # {"text": "eu não creio", "intent": "negative", "entities": []},
                # {"text": "eu não acredito", "intent": "negative", "entities": []},
                # {"text": "eu acredito", "intent": "affirmative", "entities": []},
                # {"text": "eu não faço", "intent": "negative", "entities": []},
                # {"text": "eu faço", "intent": "affirmative", "entities": []},
                # {"text": "si", "intent": "affirmative", "entities": []},
                # {"text": "sim", "intent": "affirmative", "entities": []}
            ],
        },
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.send_training_backend_nlu_persistor",
        return_value={},
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_traininglog_nlu",
        return_value={},
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_trainfail_nlu",
        return_value={},
    )
    def test_train_bert(self, *args):

        train_update(
            self.current_update.get("current_version_id"),
            self.current_update.get("repository_authorization_user_id"),
            self.repository_authorization
        )

    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_save_queue_id",
        return_value={},
    )

    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_start_training_nlu",
        return_value={
            "language": "generic_language",
            "repository_version": 6647,
            "repository_uuid": "e1e8a0fa-625c-4ba3-8b91-4c9f308db791",
            "intent": [],
            "total_training_end": 4,
            "use_name_entities": False,
            "use_competing_intents": False,
            "use_analyze_char": False
        },
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_get_examples",
        return_value={
            "count": 358,
            "next": None,
            "previous": None,
            "results": [
                {"text": "ss", "intent": "affirmative", "entities": []},
                {"text": "okay", "intent": "affirmative", "entities": []},
                {"text": "afirmativo", "intent": "affirmative", "entities": []},
                {"text": "okk", "intent": "affirmative", "entities": []},
                {"text": "okayy", "intent": "affirmative", "entities": []},
                {"text": "certo", "intent": "affirmative", "entities": []},
                {"text": "nops", "intent": "negative", "entities": []},
                {"text": "no", "intent": "negative", "entities": []},
                {"text": "nope", "intent": "negative", "entities": []},
                {"text": "não sei", "intent": "doubt", "entities": []},
                {"text": "naa", "intent": "negative", "entities": []},
                {"text": "na", "intent": "negative", "entities": []},
                {"text": "não", "intent": "negative", "entities": []},
                {"text": "talvez nao", "intent": "negative", "entities": []},
                {"text": "nnn", "intent": "negative", "entities": []}
            ],
        }
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.send_training_backend_nlu_persistor",
        return_value={},
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_traininglog_nlu",
        return_value={},
    )
    @patch(
        "bothub_backend.bothub.BothubBackend.request_backend_trainfail_nlu",
        return_value={},
    )
    def test_train_transformer_diet(self, *args):
        train_update(
            self.current_update.get("current_version_id"),
            self.current_update.get("repository_authorization_user_id"),
            self.repository_authorization
        )
