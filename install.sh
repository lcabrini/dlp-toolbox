#! /bin/sh

# Help vim out:
# vim: ft=zsh

which dnf > /dev/null 2>&1
has_dnf=$?
which yum > /dev/null 2>&1
has_yum=$?
which apt > /dev/null 2>&1
has_apt=$?

if [ -z "$RUNNING_ZSH" ]; then
    which zsh > /dev/null 2>&1
    if [ "$?" -ne "0" ]; then
        if [ "$has_dnf" -eq "0" ]; then
            dnf -y install zsh
        elif [ "$has_yum" -eq "0" ]; then
            yum -y install zsh
        elif [ "$has_apt" -eq "0" ]; then
            apt -y install zsh
        else
            echo "Cannot install zsh" >&2
            exit 1
        fi
    fi

    export RUNNING_ZSH=1
    zsh $0 "$@"
    exit $?
fi

for p in has_dnf has_yum has_apt; do
    if $p; then
        pkgman=$p
        break
    fi
done

# From this point on we should be running zsh. *phew*
if ! whence git > /dev/null 2>&1; then
    case $pkgman in
        (dnf)
            dnf -y install git
            ;;

        (yum)
            yum -y install git
            ;;

        (apt)
            apt -y install git
            ;;

        (*)
            print "we should not be here..."
            exit 1
    esac
fi

