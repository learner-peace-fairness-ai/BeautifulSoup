import time
from random import uniform

def human_wait(min_sec=0.8, max_sec=1.5):
  """人間っぽい0.8～1.5秒のランダム待機.

  さらに配慮するなら1.5〜3.0秒."""
    time.sleep(uniform(min_sec, max_sec))
