###############################################################################
#                                   PYTHON;
################################################################################
# PVM="/Python312"                    # Python interpreter (Virtual Machine)
# TKI="/Python312/libs"               # tkinter (TK graphical user Interface)
# PXE="/Python312/Scripts"            # Python eXecutablE scripts, e.g. pip (dependency management)
# PIL="/Python312/Lib"                # Python Internal Library (standard)
# PXL="/Python312/Lib/site-packages"  # Python External Library (3rd party packages)
#################################< VERSION >####################################
PYTHON_VERSIONS=("3.12.2")
# PYTHON_VERSIONS=("3.8.10" "3.9.13" "3.10.11" "3.11.2" "3.12.2")
##################################< USAGE >#####################################
# _DESTROY_ENV # (1) reset
# _INIT_PYTHON # (1) initialize
# echo -e "Current PATH: $(echo $PATH | tr ':' '\n')\n\n\n"   # (2) PATH check
# _INIT_ENV_PYTHON                                            # (2) Env Setup
# echo -e "Current PATH: $(echo $PATH | tr ':' '\n')\n\n\n"   # (2) PATH check
# python --version    # (3) Version Check
# pip --version       # (3) Version Check
# scons --version     # (3) Version Check
###############################################################################
PYTHON_URL="https://www.python.org/ftp/python/{VERSION}/python-{VERSION}-embed-amd64.zip"
PYTHON_DIR="${EXT_DIR_ABS}/Python{VERSION}"
function _INIT_PYTHON {                                         # Installation
    curl -o "get-pip.py" "https://bootstrap.pypa.io/get-pip.py"
    for ver in "${PYTHON_VERSIONS[@]}"; do
        url="${PYTHON_URL//\{VERSION\}/$ver}"
        echo $url
        ver=$(echo "$ver" | awk -F. '{print $1 $2}')
        init_ext "$url" "python.zip" "${EXT_DIR_ABS}/Python$ver"
        echo -e "python$ver.zip\n.\nimport site" > "$EXT_DIR_ABS/Python$ver/python$ver._pth"
        ${PYTHON_DIR//\{VERSION\}/$ver}/python "get-pip.py"  # Package Installer for Python
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install scons       # build automation
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install setuptools    # autobuild, src/built distro
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install --upgrade setuptools wheel
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install pipreqs --use-pep517
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install pyinstaller   # autobuild, standalone-exe distro
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install tox         # test automation
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install pytest        # autotest, testing framework
    done
    rm "get-pip.py"
}
LOCAL_PACKAGES=$(                      # .pth file contents using a `heredoc`: PYTHONPATH setup
cat << EOF
$(wpath $(pwd))
$(wpath $(pwd)/Ydqt)
$(wpath $(pwd)/phys2211)
$(wpath $(pwd)/cs4460)
... add more paths of local packages you are working on (customized packages and modules) 
EOF
)
function _INIT_ENV_PYTHON {                                         # Environment Setup
    for ver in "${PYTHON_VERSIONS[@]}"; do
        ver=$(echo "$ver" | awk -F. '{print $1 $2}')
        export PATH="${PYTHON_DIR//\{VERSION\}/$ver}:${PATH}"
        export PATH="${PYTHON_DIR//\{VERSION\}/$ver}/Scripts:${PATH}"
        echo "$LOCAL_PACKAGES" > "$EXT_DIR_ABS/Python$ver/local-packages.pth" # PYTHONPATH setup
    done
}





_DESTROY_ENV # (1) reset
_INIT_PYTHON # (1) initialize