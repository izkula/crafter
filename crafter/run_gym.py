# import gym
import crafter
import numpy as np

# env = gym.make('CrafterReward-v1')  # Or CrafterNoReward-v1
env = crafter.Env(
    seed=1,
    zombie_spawn_prob=0, skeleton_spawn_prob=0)
env = crafter.Recorder(
  env, '~/logdir/crafter/',
  save_stats=True,
  save_video=False,
  save_episode=False,
)

obs = env.reset()
done = False
while not done:
  action = int(np.random.uniform(0, env.action_space.n))
  # action = env.action_space.sample()
  obs, reward, done, info = env.step(action)
  if env._sem_view._obj_ids[crafter.objects.Zombie] in info['semantic']:
      print('Zombie!')
  if env._sem_view._obj_ids[crafter.objects.Skeleton] in info['semantic']:
      print('Skeleton!')