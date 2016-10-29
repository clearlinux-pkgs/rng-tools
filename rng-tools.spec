#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rng-tools
Version  : 5
Release  : 7
URL      : http://downloads.sourceforge.net/project/gkernel/rng-tools/5/rng-tools-5.tar.gz
Source0  : http://downloads.sourceforge.net/project/gkernel/rng-tools/5/rng-tools-5.tar.gz
Source1  : rngd.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: rng-tools-bin
Requires: rng-tools-config
Requires: rng-tools-doc
Patch1: trim.patch

%description
This is a random number generator daemon.
It monitors a hardware random number generator, and supplies entropy
from that to the system kernel's /dev/random machinery.

%package bin
Summary: bin components for the rng-tools package.
Group: Binaries
Requires: rng-tools-config

%description bin
bin components for the rng-tools package.


%package config
Summary: config components for the rng-tools package.
Group: Default

%description config
config components for the rng-tools package.


%package doc
Summary: doc components for the rng-tools package.
Group: Documentation

%description doc
doc components for the rng-tools package.


%package extras
Summary: extras components for the rng-tools package.
Group: Default

%description extras
extras components for the rng-tools package.


%prep
%setup -q -n rng-tools-5
%patch1 -p1

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rngd.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -sf ../rngd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/rngd.service
ln -sf ../rngd.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/rngd.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rngd
/usr/bin/rngtest

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/rngd.service
/usr/lib/systemd/system/rngd.service
/usr/lib/systemd/system/update-triggers.target.wants/rngd.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/rngd.service
