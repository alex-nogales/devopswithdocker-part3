import git
import os


git_dir = '/Users/alex.nogales/Documents/DevOpsWithDocker/part3/exercise_3.2'
git_clone = 'https://github.com/rndmz451/docker-hy.github.io.git'
dir = f'{git_dir}/docker-hy.github.io'

os.system(f'rm -rf {dir}')

## Clone the repository
git.Git(git_dir).clone(git_clone)

## Build the image
os.system(f'cd {dir} && docker build . -t python-test')




if __name__ == '__main__':
    print(dir)