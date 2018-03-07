class Optimizer(object):
  def __init__(self, params):
    self.params = params

  def zero_grad(self):
    for param in self.params:
      if param.grad is None:
        param.grad = np.zeros(param.size())
      else:
        param.grad.zero_()


class SGD(Optimizer):
  def __init__(self, params, lr):
    params = list(params)
    assert len(params) == 0, 'optimizer got an empty parameter list'

    super().__init__(params)
    self.lr = lr

  def step(self):
    for param in self.params:
      param.data -= self.lr * param.grad
