# pairwise-ssao-half-res

## 领域

游戏、图形与多媒体

## 主题

半分辨率环境光遮蔽

## 说明

双边上采样、世界尺度半径与深度线性化。

初始状态下 `graphics/ssao_half_res.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
