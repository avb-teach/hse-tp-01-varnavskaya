#!/bin/bash

input_dir="$1"
output_dir="$2"
if [ "$#" -ne 2 ]; then
  echo "Использование: $0 /путь/к/входной_директории /путь/к/выходной_директории"
  exit 1
fi
if [ ! -d "$input_dir" ]; then
  echo "Ошибка: входная директория '$input_dir' не существует."
  exit 1
fi
mkdir -p "$output_dir"
find "$input_dir" -type f
find "$input_dir" -type f | while read -r file; do
  filename=$(basename "$file")
  cp "$file" "$output_dir/$filename"
done
