#!/bin/bash

cat > show-info.sh << 'EOF'
#!/bin/bash

cat -e << INFO
The current directory is: $PWD
The default paths are: $PATH
The current user is: $USER
INFO

EOF

chmod +x show-info.sh