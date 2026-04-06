from IPython.display import display, Latex

def my_display_of_tensor_product(state1, state2):
    """Display the tensor product of two Qiskit Statevectors as LaTeX."""

    latex1 = state1.draw("latex_source")
    latex2 = state2.draw("latex_source")
    combined_latex = r"\left(" + latex1 + r"\right) \otimes \left(" + latex2 + r"\right)"
    display(Latex(r"$$" + combined_latex + r"$$"))


def my_display_of_tensor_products(states):
    """Display the tensor product of an array of Qiskit Statevectors as Latex."""

    states_as_latex_source = [state.draw("latex_source") for state in states]
    combined_latex = r" \otimes ".join([r"\left(" + latex + r"\right)" for latex in states_as_latex_source])
    display(Latex(r"$$" + combined_latex + r"$$"))


def my_latex_source_for_tensor_products(states):
    """Return the LaTeX source string for a tensor product."""

    states_as_latex_source = [state.draw("latex_source") for state in states]
    combined_latex = r" \otimes ".join([r"\left(" + latex + r"\right)" for latex in states_as_latex_source])
    return combined_latex


def my_display_of_schmidt_decomposition(terms):
    """Display as Latex the output of the Qiskit schmidt_decomposition function.

    ``terms`` is expected to be an iterable of tuples/lists like (amplitude, stateA, stateB, ...)
    where the first element is the amplitude and the following elements are the factors
    composing the tensor product for that term.
    """

    terms_as_latex_source = [my_latex_source_for_tensor_products(term[1:]) for term in terms]
    amplitudes = [term[0] for term in terms]
    combined_latex = r"\quad+\quad".join([f"{amplitudes[i]:.3g}" + r"\times" + terms_as_latex_source[i] for i in range(len(terms))])
    display(Latex(r"$$" + combined_latex + r"$$"))


__all__ = [
    "my_display_of_tensor_product",
    "my_display_of_tensor_products",
    "my_display_of_schmidt_decomposition",
]
