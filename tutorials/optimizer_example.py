import tensorflow as tf

# Sessions
session = tf.Session()

# Loss functions and optimizers
# Training and testing
# Introduce the concepts and look at some examples

# # loss function: actual vs expected outputs
# # actual: output from our model given an input
# # expected: correct output given an input
#
# # Optimizers: change values in model to alter loss (typically to minimize)
#
# # Values altered during training
# # Model assessed during testing
#Warning this program produce TypeError: unsupported operand type(s) for -: 'list' and 'list'
# this program just demonstrate the way
x_train = [1.0, 2.0, 3.0, 4.0]
y_train = [2.0, 3.0, 4.0, 5.0]
y_actual = [1.5, 2.5, 3.5, 4.5]
loss = tf.reduce_sum(input_tensor=tf.square(x=y_train - y_actual))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05)
train_step = optimizer.minimize(loss=loss)
