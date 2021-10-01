# Import package, test suite, and other packages as needed
import mmic_cg
import pytest
from mmic.components.blueprints import TacticComponent
import mm_data
from typing import Tuple
import sys
import json


mol_file = mm_data.mols["water-mol.json"]
#ff_file = mm_data.ffs["water-ff.json"]


def test_mmic_cg_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_cg" in sys.modules


def test_mmic_cg_models():
    with open(mol_file, "r") as fp:
        mol = json.load(fp)

    inputs = mmic_cg.InputCoarse(
        molecule={"mol": mol},
        schema_name="test",
        schema_version=1.0,
        method="spacewarping",
    )

    class CoarseDummyComponent(TacticComponent):
        @classmethod
        def input(cls):
            return mmic_cg.InputCoarse

        @classmethod
        def output(cls):
            return mmic_cg.OutputCoarse

        @classmethod
        def strategy_comps(cls):
            return mmic_cg.CoarseComponent

        @classmethod
        def get_version(cls):
            return None

        def execute(
            self,
            inputs: mmic_cg.InputCoarse,
        ) -> Tuple[bool, mmic_cg.OutputCoarse]:

            return True, mmic_cg.OutputCoarse(proc_input=inputs, molecule=inputs.molecule, schema_name=inputs.schema_name, schema_version=inputs.schema_version, success=True)

    outputs = CoarseDummyComponent.compute(inputs)
