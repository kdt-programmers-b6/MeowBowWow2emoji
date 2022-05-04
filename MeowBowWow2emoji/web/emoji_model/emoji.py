import tensorflow as tf 
import cv2 #사용
import numpy as np
import os
from .UGATIT_noargs import UGATIT


# import matplotlib.pyplot as plt
class Emoji:
  def __init__(self,checkpoint_path,args):
    tf.reset_default_graph()
    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
    gan = UGATIT(args)
    gan.build_model()
    saver = tf.train.Saver()
    saver.restore(sess, checkpoint_path)
    self.sess = sess
    self.gan = gan
  
  def selfie2anime(self ,img_path):
    img = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    brightness = 0
    contrast = 30
    img = np.int16(img)
    img = img * (contrast / 127 + 1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)

    # preprocessing
    img_input = cv2.resize(img, dsize=(256, 256), interpolation=cv2.INTER_NEAREST)
    img_input = np.expand_dims(img_input, axis=0)
    img_input = img_input / 127.5 - 1

    # inference
    img_output = self.sess.run(self.gan.test_fake_B, feed_dict={self.gan.test_domain_A: img_input})

    # postprocessing
    img_output = (img_output + 1) * 127.5
    img_output = img_output.astype(np.uint8).squeeze()
        
    #result = np.hstack([cv2.resize(img, (256, 256)), img_output])
        
    #plt.figure(figsize=(16, 8))
    #plt.axis('off')
    #plt.imshow(img_output)
    cv2.imwrite(os.getcwd()+'/media/result/%s' % os.path.basename(img_path), img_output[:, :, ::-1])
    return open(os.getcwd()+'/media/result/'+os.path.basename(img_path), 'rb')
    #return img_output

def parse_args():
    parser = {}
    parser['light']=False
    parser['dataset']='selfie2anime'

    parser['epoch']=100
    parser['iteration']=10000
    parser['batch_size']=1
    parser['print_freq']=1000
    parser['save_freq']=10000
    parser['decay_flag']=True
    parser['decay_epoch']=50

    parser['lr']=0.0001
    parser['GP_ld']=10
    parser['adv_weight']=1
    parser['cycle_weight']=10
    parser['identity_weight']=10
    parser['cam_weight']=1000
    parser['gan_type']='lsgan'

    parser['smoothing']=True

    parser['ch']=16
    parser['n_res']=4
    parser['n_dis']=6
    parser['n_critic']=1
    parser['sn']=True

    parser['img_size']=256
    parser['img_ch']=3
    parser['augment_flag']=True
    
    parser['checkpoint_dir']='checkpoint'
    parser['result_dir']='results'
    parser['log_dir']='logs'
    parser['sample_dir']='samples'

    return parser