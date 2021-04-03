function bh_install_vim_runtime {
    __DOC__ 'bh_install_vim_runtime --> install'
    git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
    sh ~/.vim_runtime/install_awesome_vimrc.sh
}

