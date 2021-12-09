#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-requests_download
Version  : 0.1.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/34/9d/431a25538f158a3065a76a6311f40b7908f88a4d24efdbb0ca24f83bd614/requests_download-0.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/9d/431a25538f158a3065a76a6311f40b7908f88a4d24efdbb0ca24f83bd614/requests_download-0.1.2.tar.gz
Summary  : Download files using requests and save them to a target path
Group    : Development/Tools
License  : MIT
Requires: pypi-requests_download-license = %{version}-%{release}
Requires: pypi-requests_download-python = %{version}-%{release}
Requires: pypi-requests_download-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit)

%description
A convenient function to download to a file using requests.
Basic usage:
.. code-block:: python

%package license
Summary: license components for the pypi-requests_download package.
Group: Default

%description license
license components for the pypi-requests_download package.


%package python
Summary: python components for the pypi-requests_download package.
Group: Default
Requires: pypi-requests_download-python3 = %{version}-%{release}

%description python
python components for the pypi-requests_download package.


%package python3
Summary: python3 components for the pypi-requests_download package.
Group: Default
Requires: python3-core
Provides: pypi(requests_download)
Requires: pypi(requests)

%description python3
python3 components for the pypi-requests_download package.


%prep
%setup -q -n requests_download-0.1.2
cd %{_builddir}/requests_download-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639059865
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-requests_download
cp %{_builddir}/requests_download-0.1.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-requests_download/cfa8b1d835b4a9fd4f13fb578f53b10d47c1a0a0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-requests_download/cfa8b1d835b4a9fd4f13fb578f53b10d47c1a0a0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
