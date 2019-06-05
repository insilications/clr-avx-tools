#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-avx-tools
Version  : 7
Release  : 8
URL      : https://github.com/clearlinux/clr-avx-tools/archive/v7.tar.gz
Source0  : https://github.com/clearlinux/clr-avx-tools/archive/v7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clr-avx-tools-bin
Requires: clr-avx-tools-data
Requires: clr-avx-tools-license

%description
No detailed description available

%package bin
Summary: bin components for the clr-avx-tools package.
Group: Binaries
Requires: clr-avx-tools-data
Requires: clr-avx-tools-license

%description bin
bin components for the clr-avx-tools package.


%package data
Summary: data components for the clr-avx-tools package.
Group: Data

%description data
data components for the clr-avx-tools package.


%package license
Summary: license components for the clr-avx-tools package.
Group: Default

%description license
license components for the clr-avx-tools package.


%prep
%setup -q -n clr-avx-tools-7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536432575
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1536432575
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/clr-avx-tools
cp COPYING %{buildroot}/usr/share/doc/clr-avx-tools/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-avx2-move.pl
/usr/bin/clr-python-avx2
/usr/bin/clr-python-avx512

%files data
%defattr(-,root,root,-)
/usr/share/clr-avx-tools/avxjudge.make
/usr/share/clr-avx-tools/avxjudge.py

%files license
%defattr(-,root,root,-)
/usr/share/doc/clr-avx-tools/COPYING
