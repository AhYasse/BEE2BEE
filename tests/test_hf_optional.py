def test_run():
    # HF may not be installed; just check capability flag and import path
    from bee2bee.hf import has_transformers, has_datasets
    assert isinstance(has_transformers(), bool)
    assert isinstance(has_datasets(), bool)

