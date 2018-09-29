import tensorflow as tf

#Sessions
session=tf.Session()

# Variable node 
#When and how to use them
#Compare to constant node


var_1=tf.Variable(initial_value=[3.0],
                  trainable=True,
                  collections=None,
                  validate_shape=True,
                  caching_device=None,
                  name='var_1',
                  variable_def=None,
                  dtype=tf.float32,
                  expected_shape=(1,None),
                  import_scope=None)


print(var_1)
init=tf.global_variables_initializer()
session.run(init)
print(session.run(fetches=var_1))

var_2=var_1.assign(value=[4.0])
print(session.run(fetches=var_1))
print(session.run(fetches=var_2))
