import os


def test_project_folder_in_place(root_dir, project_dirname):
    manage_rpath = os.path.join(project_dirname, 'manage.py')
    manage_fpath = os.path.join(root_dir, manage_rpath)

    print(f'Путь к файлу manage.py: {manage_fpath}')
    print(f"Ожидаемый путь к файлу manage.py: {manage_fpath}")

    assert os.path.isfile(manage_fpath), (
        f'Не найден файл `{manage_rpath}`. '
        'Убедитесь, что структура проекта соответствует заданию.'
    )
