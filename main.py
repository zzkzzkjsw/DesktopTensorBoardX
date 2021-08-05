from tensorboardX import SummaryWriter
writer = SummaryWriter('runs/scalar_example')
for i in range(10):
    writer.add_scalar('quadratic', i**2, global_step=i)
    writer.add_scalar('exponential', 2**i, global_step=i)


# 对github说一点声明：注意vpn，否则可能产生403错误
# 只需下载tensorboardX即可
# cmd中运行：tensorboard --logdir C:\Users\zzk56\Desktop\TensorBoardX\runs\scalar_example