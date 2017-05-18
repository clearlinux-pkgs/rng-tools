#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rng-tools
Version  : 5
Release  : 15
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
Patch2: feed-more.patch

%description
This is a random number generator daemon.
It monitors a hardware random number generator, and supplies entropy
from that to the system kernel's /dev/random machinery.

%package autostart
Summary: autostart components for the rng-tools package.
Group: Default

%description autostart
autostart components for the rng-tools package.


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


%prep
%setup -q -n rng-tools-5
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493604097
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493604097
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rngd.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sf ../rngd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/rngd.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/rngd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/rngd
/usr/bin/rngtest

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/rngd.service
/usr/lib/systemd/system/rngd.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*
