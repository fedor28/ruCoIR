# ruCoIR Датасет

ruCoir датасет переведен с использованием phi4 на русский. Передены некоторые задания: apps, codefeedback-st, stackoverflow-qa, cosqa, codesearchnet.

## Запуск замеров

Для запуска замеров выполните следующую команду:
```bash
python sentence_transformermers_run_eval.py /\
  --model_name ai-forever/FRIDA \
  --tasks apps codefeedback-st stackoverflow-qa cosqa codesearchnet \
  --batch_size 128 \
  --hf_token hf_...
```
Результаты сохраняются в папке `results`.

Для замера по Api Voyager. URL захардкожен.

```bash
python API_retrival_run_eval.py \
  --model_name voyage-code-3\
  --tasks apps codefeedback-st stackoverflow-qa cosqa codesearchnet \
  --batch_size 128 \
  --hf_token hf_...
```
## Чтение результатов

Чтобы прочитать результаты, выполните одну из следующих команд:

- Для чтения результатов для конкретной модели:
  python read_scores.py ./results/model_name

- Для чтения всех замеров по всем моделям:
  python read_scores_all.py ./results. Результат будет сохранен в файл `results.csv`.

## Результаты замеров открытых моделей
| Model                                   | apps.  | codefeedback-st. | stackoverflow-qa. | cosqa.  | CodeSearchNet-go. | CodeSearchNet-java. | CodeSearchNet-javascript. | CodeSearchNet-ruby. | CodeSearchNet-python. | CodeSearchNet-php. |
|-----------------------------------------|--------|-------------------|-------------------|---------|--------------------|----------------------|-----------------------------|----------------------|------------------------|---------------------|
| intfloat/multilingual-e5-small          | 0.12454| 0.71173           | 0.81983           | 0.26235 | 0.53938            | 0.48008              | 0.44266                     | 0.54329              | 0.69071                | 0.61809             |
| intfloat/multilingual-e5-large          | 0.22446| 0.85074           | 0.91129           | 0.36054 | 0.74568            | 0.69757              | 0.5711                      | 0.76146              | 0.78986                | 0.76049             |
| intfloat/e5-mistral-7b-instruct         | 0.22807| 0.86789           | **0.95361**           | 0.32366 | 0.74161            | 0.63436              | 0.4863                      | 0.66865              | 0.65875                | 0.59292             |
| intfloat/multilingual-e5-large-instruct | 0.25247| 0.84635           | 0.93297           | 0.35589 | 0.71499            | 0.65654              | 0.47934                     | 0.6995               | 0.70834                | 0.79527             |
| ai-sage/Giga-Embeddings-instruct        | 0.19977| 0.86981           | 0.91166           | 0.32218 | 0.72875            | 0.61496              | 0.39666                     | 0.61142              | 0.61774                | 0.55708             |
| ai-forever/FRIDA                        | 0.04442| 0.68872           | 0.70922           | 0.18806 | 0.78615            | 0.69715              | 0.57283                     | 0.71219              | 0.79364                | 0.77919             |
| Alibaba-NLP/gte-modernbert-base         | 0.3561 | 0.73569           | 0.87665           | 0.21053 | 0.7472             | 0.68181              | 0.59494                     | 0.67936              | 0.59185                | 0.80744             |
| Alibaba-NLP/gte-Qwen2-1.5B-instruct     | 0.28074| 0.90932           | 0.90666           | 0.34666 | 0.6536             | 0.79168              | 0.64452                     | 0.75967              | 0.77614                | 0.87361             |
| Salesforce/SFR-Embedding-Code-2B_R      | 0.84602| 0.92086           | 0.93166           | 0.37536 | 0.85252            | 0.75598              | 0.69642                     | **0.89186**              | 0.86977                | 0.82265             |
| Salesforce/SFR-Embedding-Code-400M_R    | 0.15948| 0.44374           | 0.66554           | 0.09348 | 0.67125            | 0.38164              | 0.37816                     | 0.4544               | 0.46947                | 0.52578             |
| codesage/codesage-large-v2              | 0.44837| 0.68421           | 0.7987            | 0.18018 | 0.82199            | 0.7695               | 0.73225                     | 0.85043              | 0.78738                |-                    |
| voyage-code-3                           | 0.42881| 0.91742           | 0.91549           | **0.46808** | —                  | —                    | —                           | —                    | —                      | —                   |
| Alibaba-NLP/gte-multilingual-base       | 0.1396 | 0.84446           | 0.85687           | 0.25893 | 0.84667            | 0.80893              | 0.7454                      | 0.79466              | **0.88632**                | 0.89419             |
| BAAI/bge-code-v1                    | **0.96076** | **0.95732** | 0.94251 | 0.30005 | **0.87277** | **0.87529** | **0.77994** | **0.89577** | 0.83198 | **0.91181** |

