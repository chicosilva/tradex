from base64 import b64encode
from functools import reduce
from operator import or_

from config.settings import MEDIA_ROOT
from django.db.models import Q


def clean_cpf(value):
    return value.replace(".", "").replace("-", "")


def clean_cnpj(value):
    return value.replace(".", "").replace("-", "").replace("/", "")


def clean_cep(value):
    return value.replace(".", "").replace("-", "")


def mount_multifield_filter(values: list, fields: list, numeric_fields: list = None):
    values, query = values.split(" "), Q()

    for val in values:
        val_clean = clean_cpf(val)
        if val_clean.isnumeric() and numeric_fields is not None:
            query &= reduce(or_, [Q(**{f"{f}__icontains": val_clean}) for f in numeric_fields])
        else:
            query &= reduce(or_, [Q(**{f"{f}__icontains": val}) for f in fields])
    return query


def mount_state_full_name(initials, name):
    value = name
    if initials is None or name is None:
        value = None

    elif initials in ["AC", "AP", "AM", "CE", "ES", "MA", "MT", "MS", "PR", "PA", "PI", "RJ", "RN", "RS", "TO"]:
        value = f"Estado do {name}"

    elif initials in ["AL", "GO", "MG", "PE", "RO", "RR", "SC", "SP", "SE"]:
        value = f"Estado de {name}"

    elif initials in ["BA", "PB"]:
        value = f"Estado da {name}"
    return value


def check_image_size(image_base64):
    if not image_base64 or image_base64 == "":
        return 0
    if isinstance(image_base64, str):
        tamanho = (len(image_base64) * 3) / 4 - image_base64.count("=", -2)
    else:
        tamanho = 0
    return tamanho


def encode_pdf(file_path):
    file_path = str(MEDIA_ROOT) + "/" + str(file_path).replace("/media", "")
    with open(file_path, "rb") as pdf_file:
        encoded_string = b64encode(pdf_file.read())
    return encoded_string


def clean_parametros_busca(parametros_busca):
    param_mutable = parametros_busca.copy()
    params = ["page", "page_size", "ordering", "search"]
    for item in list(param_mutable):
        if item in params:
            del param_mutable[item]

    return param_mutable
