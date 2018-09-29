import tensorflow as tf

# Sessions
session = tf.Session()
# Operation nodes
# How to perform operations on existing nodes
# Build a mini computational graph
# Operation nodes perform some operation on one or more nodes and store result

const_1 = tf.constant(value=[1.0])
const_2 = tf.constant(value=[4.0])
placeholder_1 = tf.placeholder(dtype=tf.float32)
#results = const_1 + const_2
#results = tf.add(x=const_1, y=const_2, name='results')
results = tf.add(x=placeholder_1, y=const_2, name='results')
#print(session.run(fetches=results))
#
# # y = Wx + b
W = tf.constant(value=[2.0])
b = tf.constant(value=[1.0])
x = tf.placeholder(dtype=tf.float32)
#y = W * x + b
mult = tf.multiply(x=W, y=x)
y = tf.add(x=mult, y=b)

# print(session.run(fetches=results, feed_dict={placeholder_1: [2.0]}))
#print(session.run(fetches=y, feed_dict={x: [2.0]}))
print(session.run(fetches=y, feed_dict={x: [2.0, 3.0, 4.0]}))
