@echo off
color f

echo info for packages at https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

echo updating pkg:

echo pytest:
python setup.py pytest 
echo pytest - finished

echo bdist_wheel:
python setup.py bdist_wheel
echo bdist_wheel - done

echo going to dist:
cd dist
echo going to dist - done

echo reinstalling pkg:
pip install PGB-0.1.0-py3-none-any.whl --force-reinstall
echo reinstalling pkg - done

echo going to prev directory:
cd ..
echo going to prev directory - done

echo finished everything!