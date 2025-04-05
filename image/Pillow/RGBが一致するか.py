def matches_rgb(
    rgb1: tuple[int, int, int], rgb2: tuple[int, int, int], tolerance: int = 0
) -> bool:
    """RGBが一致するか調べる

    誤差を指定できる.

    Parameters:
        rgb1 (tuple[int, int, int]):
        rgb2 (tuple[int, int, int]):
        tolerance (int): RGB値の誤差。デフォルトは0.

    Returns:
        bool:
    """
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(rgb1, rgb2))
