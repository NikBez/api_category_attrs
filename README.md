# API показывает аналитику по атрибутам продукта и модифицированную аннотацию/добавляет фото
Скрипт не меняет данные в таблице просто выводит в модифицированном виде 

### Требования перед запуском:

- Используй Poetry (или другую библиотеку) для установки зависимостей;
```bash
poetry install
```
- Необходимо заполнить файл .env по примеру в файле .env_example

### Описание 
- Необходимо заполнить поля **category_id** и **product_id** 
- Получаем ответ в виде:
````
{
  "total_count": 0,
  "blank_percentage": 0,
  "annotation_length": 0,
  "images_count": 0,
  "modified_annotation": "string",
  "modified_images": "string"
}
````

### Для запуска скрипта:
````bash
uvicorn main:app --reload
````
````bash
uvicorn main:app
127.0.0.1:8000/docs
````
