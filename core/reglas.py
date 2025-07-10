def aplicar_evento(estado, evento):
    if not evento:
        return estado

    objetivo = evento["afecta"]
    propiedad = evento["modifica"]
    valor = evento["valor"]

    # Asegurar que la propiedad exista
    if propiedad not in estado[objetivo]:
        estado[objetivo][propiedad] = 0

    estado[objetivo][propiedad] += valor

    # Evitar valores negativos
    estado[objetivo][propiedad] = max(0, estado[objetivo][propiedad])

    return estado
