import tensorflow as tf

#Sessions
session=tf.Session()

# Placeholder Node
# When and how to use them
#Comapare to Variable and Constant nodes
 
placeholder_1=tf.placeholder(dtype=tf.float32,
                              shape=(1,4),
                              name='placeholder_1')
placeholder_2=tf.placeholder(dtype=tf.float32,
                              shape=(2,2),
                              name='placeholder_2')
 
print(placeholder_1)
print(session.run(fetches=[placeholder_1,placeholder_2],
                  feed_dict={placeholder_1:[[1.0,3.0,4.0,8.0]],placeholder_2:[[1.0,3.0],[4.0,5.0]]}))
