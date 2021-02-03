#!/bin/bash
echo "Hello world!"

your_name='LiMing'
echo $your_name # not recommend
echo ${your_name}  # recommend

your_name="Tom"
echo $your_name
your_name="alibaba"
echo $your_name

myUrl="https://www.google.com"
readonly myUrl
myUrl="https://www.runoob.com"

myUrl0="https://www.runoob.com"
unset myUrl0
echo $myUrl0
#!/bin/bash
echo "Hello world!"

your_name='LiMing'
echo $your_name # not recommend
echo ${your_name}  # recommend

your_name="Tom"
echo $your_name
your_name="alibaba"
echo $your_name

myUrl="https://www.google.com"
readonly myUrl
myUrl="https://www.runoob.com"

myUrl0="https://www.runoob.com"
unset myUrl0
echo $myUrl0