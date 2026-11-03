def print_models(unprinted_designs, completed_models):
    """
    Simulasikan pencetakan tiap desain sampai habis.
    Pindahkan tiap desain ke completed_models setelah dicetak.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Tampilkan semua model yang sudah dicetak."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)