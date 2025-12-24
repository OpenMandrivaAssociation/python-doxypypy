%define module doxypypy

Name:		python-doxypypy
Version:	0.8.8.7
Release:	2
Summary:	Doxygen filter for Python
License:	GPL
Group:		Development/Python
URL:		https://pypi.org/project/doxypypy/
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch: noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
For now Doxygen has limited support for Python. It recognizes Python comments,
but otherwise treats the language as being more or less like Java. It doesn’t
understand basic Python syntax constructs like docstrings, keyword arguments,
generators, nested functions, decorators, or lambda expressions.

It likewise doesn’t understand conventional constructs like doctests or
ZOPE-style interfaces. It does however support inline filters that can be
used to make input source code a little more like what it’s expecting.

The excellent doxypy makes it possible to embed Doxygen commands in Python
docstrings, and have those docstrings converted to Doxygen-recognized
comments on the fly per Doxygen’s regular input filtering process.
It however does not address any of the other previously mentioned areas of
difficulty.

This project started off as a fork of doxypy but quickly became quite
distinct. It shares little (if any) of the same code at this point (but
maintains the original license just in case). It is meant to support
all the same command line options as doxypy, but handle additional
Python syntax beyond docstrings.

%prep
%autosetup -p1 -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{oname}.egg-info


%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/doxypypy
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-*.*-info
