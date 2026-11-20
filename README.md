# Agente de Vagas IA

Agente que roda **todo dia às 7h15 (Fortaleza)** como tarefa agendada no Claude Code (nuvem). Ele procura vagas remotas para quem está começando a graduação em Inteligência Artificial, gera um **currículo em PDF adaptado para cada vaga** e envia tudo por e-mail.

## O que ele faz

1. **Evita repetições:** lê os e-mails "[Vagas IA]" dos últimos 30 dias e não manda a mesma vaga duas vezes.
2. **Busca vagas:** primeiro as **pagas em dólar (USD)**, depois as do **Brasil (R$)**. Inclui estágio, júnior, freelance, treinamento/avaliação de IA, transcrição, legendagem, anotação de dados e linguística.
3. **Filtra:** só vagas 100% remotas, sem exigência de diploma ou de mais de 1 ano de experiência, recentes e sem sinais de golpe.
4. **Confere:** abre a página da vaga quando o site permite (✅) ou marca como não verificada (⚠️).
5. **Adapta o currículo:** usa `curriculo/base.json` como única fonte da verdade (nunca inventa experiência) e gera um PDF de 1 página por vaga com `scripts/gen_cv.py`.
6. **Envia o e-mail:** até 7 vagas, com link, salário, nível de inglês, por que combina, dicas e os PDFs anexados.

O agente **não se candidata** a nenhuma vaga: a decisão é sempre sua.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `prompt/agente_vagas.md` | Instruções da tarefa agendada |
| `scripts/gen_cv.py` | Gera o PDF do currículo a partir de um JSON (ReportLab) |
| `curriculo/base.json` | Currículo base usado em todas as adaptações |
| `curriculo/Curriculo_Igor_Tavares_IA.pdf` | Currículo base em PDF |
| `config/allowed_hosts.txt` | Sites de vagas liberados na rede do ambiente |

## Como usar

1. Em [claude.ai/code](https://claude.ai/code), crie uma tarefa agendada diária com o texto de `prompt/agente_vagas.md` e **marque o conector Gmail**.
2. Nas configurações do ambiente, libere os sites de `config/allowed_hosts.txt`.
3. Para gerar um currículo manualmente:

```bash
pip install reportlab
```

```bash
python3 scripts/gen_cv.py curriculo/base.json meu_cv.pdf
```

## Tecnologias

Claude Code (tarefas agendadas na nuvem) · conector Gmail · Python · ReportLab

---

Feito por **Igor Barroso Tavares**, estudante de Inteligência Artificial na Unifor · [GitHub](https://github.com/igortavares2709-ops) · [LinkedIn](https://www.linkedin.com/in/igor-barroso-171b59263/)
