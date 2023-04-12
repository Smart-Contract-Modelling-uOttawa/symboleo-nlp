from __future__ import annotations

from app.src.operations.norm_builder import IBuildNorms, NormBuilder

# This class will contain a variety of functions that will be used by SelectedNodes to construct things
class SelectionTools:
    def __init__(
        self,
        norm_builder: IBuildNorms
    ):
        self.norm_builder = norm_builder

    @staticmethod
    def build() -> SelectionTools:
        norm_builder = NormBuilder()

        return SelectionTools(
            norm_builder
        )
