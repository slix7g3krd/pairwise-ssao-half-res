import pytest
import graphics.ssao_half_res as mod

CASES = [
    ("bilateral_upsample", (1,)),
    ("radius_world_scale", (1,)),
    ("linearize_depth", (1,)),
    ("reproject_validate", (1,)),
    ("exclude_transparent", (1,)),
    ("temporal_clamp", (1,)),
    ("load", (1,)),
    ("compute", (1,)),
    ("compose", (1,)),
    ("present", (1,)),
    ("validate_ssao", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
