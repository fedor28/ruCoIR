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
![image](https://github.com/fedor28/ruCoIR/blob/bge_code_model/pictures/all_results.png)

