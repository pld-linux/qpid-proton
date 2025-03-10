# TODO: package go files (where?)
#
# Conditional build:
%bcond_with	static_libs	# static libraries
%bcond_with	golang		# Go binding
%bcond_without	python		# Python binding
%bcond_without	ruby		# Ruby binding

Summary:	Qpid Proton - AMQP messaging toolkit
Summary(pl.UTF-8):	Qpid Proton - narzędzia do komunikacji AMQP
Name:		qpid-proton
Version:	0.39.0
Release:	
License:	Apache v2.0
Group:		Libraries
Source0:	https://downloads.apache.org/qpid/proton/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d910a2ec7ea874dc9f571b38285b7f82
Patch0:		no-Werror.patch
URL:		https://qpid.apache.org/proton/
BuildRequires:	cmake >= 3.16
BuildRequires:	cyrus-sasl-devel
BuildRequires:	doxygen
%{?with_golang:BuildRequires:	golang >= 1.11}
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.8
%{?with_python:BuildRequires:	python3-devel >= 1:3.8}
BuildRequires:	rpm-build >= 4.6
%{?with_ruby:BuildRequires:	ruby-devel}
%{?with_python:BuildRequires:	swig-python}
%{?with_ruby:BuildRequires:	swig-ruby}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proton is a high performance, lightweight messaging library. It can be
used in the widest range of messaging applications including brokers,
client libraries, routers, bridges, proxies, and more. Proton makes it
trivial to integrate with the AMQP 1.0 ecosystem from any platform,
environment, or language.

%description -l pl.UTF-8
Proton to wydajna, lekka biblioteka do komunikacji. Może być używana w
szerokiej gamie aplikacji komunikacyjnych, w tym brokerów, bibliotek
klienckich, routerów, mostków, proxy itp. Proton powoduje, że
integrowanie z ekosystemem AMQP 1.0 z woeolnej platformy, środowiska
czy języka staje się trywialne.

%package c
Summary:	C libraries for Qpid Proton
Summary(pl.UTF-8):	Biblioteki C Qpid Proton
Group:		Libraries

%description c
C libraries for Qpid Proton.

%description c -l pl.UTF-8
Biblioteki C Qpid Proton.

%package c-devel
Summary:	Development files for Qpid Proton C libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek Qpid Proton dla C
Group:		Development/Libraries
Requires:	%{name}-c = %{version}-%{release}

%description c-devel
Development files for writing messaging apps with Qpid Proton C
libraries.

%description c-devel -l pl.UTF-8
Pliki programistyczne do tworzenia aplikacji z wykorzystaniem
bibliotek C Qpid Proton.

%package c-apidocs
Summary:	Documentation for Qpid Proton C API
Summary(pl.UTF-8):	Dokumentacja API bibliotek C Qpid Proton
Group:		Documentation
Obsoletes:	qpid-proton-c-devel-doc < 0.31.0
BuildArch:	noarch

%description c-apidocs
Documentation for Qpid Proton C API.

%description c-apidocs -l pl.UTF-8
Dokumentacja API bibliotek C Qpid Proton.

%package cpp
Summary:	C++ libraries for Qpid Proton
Summary(pl.UTF-8):	Biblioteki C++ Qpid Proton
Group:		Libraries
Requires:	%{name}-c = %{version}-%{release}
Requires:	libstdc++-devel

%description cpp
C++ libraries for Qpid Proton.

%description cpp -l pl.UTF-8
Biblioteki C++ Qpid Proton.

%package cpp-devel
Summary:	Development files for Qpid Proton C++ library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Qpid Proton dla C++
Group:		Development/Libraries
Requires:	%{name}-c-devel = %{version}-%{release}
Requires:	%{name}-cpp = %{version}-%{release}

%description cpp-devel
Development files for writing messaging apps with Qpid Proton C++
library.

%description cpp-devel -l pl.UTF-8
Pliki programistyczne do tworzenia aplikacji z wykorzystaniem
biblioteki C++ Qpid Proton.

%package cpp-apidocs
Summary:	Documentation for Qpid Proton C++ API
Summary(pl.UTF-8):	Dokumentacja API biblioteki C++ Qpid Proton
Group:		Documentation
BuildArch:	noarch

%description cpp-apidocs
Documentation for Qpid Proton C++ API.

%description cpp-apidocs -l pl.UTF-8
Dokumentacja API biblioteki C++ Qpid Proton.

%package -n python3-%{name}
Summary:	Python language bindings for the Qpid Proton messaging framework
Summary(pl.UTF-8):	Wiązania Pythona do szkieletu komunikacji Qpid Proton
Group:		Libraries/Python
Requires:	%{name}-c = %{version}-%{release}
Obsoletes:	python-qpid-proton < 0.39

%description -n python3-%{name}
Python language bindings for the Qpid Proton messaging framework.

%description -n python3-%{name} -l pl.UTF-8
Wiązania Pythona do szkieletu komunikacji Qpid Proton.

%package -n python3-%{name}-apidocs
Summary:	Documentation for the Python language bindings for Qpid Proton
Summary(pl.UTF-8):	Dokumentacja wiązań Pythona do biblioteki Qpid Proton
Group:		Documentation
Obsoletes:	python-qpid-proton-apidocs < 0.39
Obsoletes:	python-qpid-proton-doc < 0.31.0
BuildArch:	noarch

%description -n python3-%{name}-apidocs
Documentation for the Python language bindings for Qpid Proton.

%description -n python3-%{name}-apidocs -l pl.UTF-8
Dokumentacja wiązań Pythona do biblioteki Qpid Proton.

%package -n ruby-%{name}
Summary:	Ruby language bindings for the Qpid Proton messaging framework
Summary(pl.UTF-8):	Wiązania języka Ruby do szkieletu komunikacji Qpid Proton
Group:		Development/Languages
Requires:	%{name}-c = %{version}-%{release}
Requires:	ruby-modules

%description -n ruby-%{name}
Ruby language bindings for the Qpid Proton messaging framework.

%description -n ruby-%{name} -l pl.UTF-8
Wiązania języka Ruby do szkieletu komunikacji Qpid Proton.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' \
	c/examples/testme \
	cpp/examples/testme

%{__sed} -i -e '1s,/usr/bin/env python3$,%{__python3},' \
	python/examples/*.py

%build
%cmake -B build \
	-DBUILD_BINDINGS="cpp;go%{?with_python:;python}%{?with_ruby:;ruby}" \
	%{?with_golang:-DBUILD_GO=ON} \
	%{?with_static_libs:-DBUILD_STATIC_LIBS=ON} \
	-DSYSINSTALL_PYTHON=ON
#	-DPYTHON_SITEARCH_PACKAGES=%{py_sitedir} \

%{__make} -C build all docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/proton/{CMakeLists.txt,LICENSE.txt,README.md,examples/README.md,tests}

install -d $RPM_BUILD_ROOT{%{_examplesdir},%{_docdir}/%{name}}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/examples/c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-c-%{version}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/examples/cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-cpp-%{version}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/docs/api-c $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/docs/api-cpp $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with python}
cd build/python
%py3_install
cd ../..

%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/docs/api-py $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}/api-py/{.doctrees,_sources,.buildinfo,conf.py,*.inv,*.rst}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/examples/python $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}
%endif

%if %{with ruby}

install -d $RPM_BUILD_ROOT%{_libdir}/proton/bindings/ruby
install build/ruby/cproton.so $RPM_BUILD_ROOT%{_libdir}/proton/bindings/ruby
cp -pr build/ruby/gem/lib/* $RPM_BUILD_ROOT%{_libdir}/proton/bindings/ruby
%{__mv} $RPM_BUILD_ROOT%{_datadir}/proton/examples/ruby $RPM_BUILD_ROOT%{_examplesdir}/ruby-%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	c -p /sbin/ldconfig
%postun	c -p /sbin/ldconfig

%post	cpp -p /sbin/ldconfig
%postun	cpp -p /sbin/ldconfig

%files c
%defattr(644,root,root,755)
%doc NOTICE.txt README.md
%attr(755,root,root) %{_libdir}/libqpid-proton.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpid-proton.so.11
%attr(755,root,root) %{_libdir}/libqpid-proton-core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpid-proton-core.so.10
%attr(755,root,root) %{_libdir}/libqpid-proton-proactor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpid-proton-proactor.so.1

%files c-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqpid-proton.so
%attr(755,root,root) %{_libdir}/libqpid-proton-core.so
%attr(755,root,root) %{_libdir}/libqpid-proton-proactor.so
%dir %{_includedir}/proton
%{_includedir}/proton/*.h
%{_includedir}/proton/cproton.i
%{_pkgconfigdir}/libqpid-proton.pc
%{_pkgconfigdir}/libqpid-proton-core.pc
%{_pkgconfigdir}/libqpid-proton-proactor.pc
%{_libdir}/cmake/Proton

%files c-apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/api-c
%{_examplesdir}/%{name}-c-%{version}

%files cpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqpid-proton-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpid-proton-cpp.so.12

%files cpp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqpid-proton-cpp.so
%{_includedir}/proton/*.hpp
%{_includedir}/proton/codec
%{_includedir}/proton/internal
%{_includedir}/proton/io
%{_pkgconfigdir}/libqpid-proton-cpp.pc
%{_libdir}/cmake/ProtonCpp

%files cpp-apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/api-cpp
%{_examplesdir}/%{name}-cpp-%{version}

%if %{with python}
%files -n python3-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/cproton_ffi.abi3.so
%{py3_sitedir}/cproton.py
%{py3_sitedir}/__pycache__/cproton.cpython-*.py[co]
%{py3_sitedir}/proton
%{py3_sitedir}/python_qpid_proton-%{version}-py*.egg-info

%files -n python3-%{name}-apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/api-py
%{_examplesdir}/python-%{name}-%{version}
%endif

%if %{with ruby}
%files -n ruby-%{name}
%defattr(644,root,root,755)
%if 0
# cannot use SYSINSTALL_RUBY for now because...
%attr(755,root,root) %{ruby_vendorarchdir}/cproton.so
%{ruby_vendorarchdir}/qpid_proton.rb
# the files below are likely to conflict with other ruby packages
%{ruby_vendorarchdir}/codec
%{ruby_vendorarchdir}/core
%{ruby_vendorarchdir}/handler
%{ruby_vendorarchdir}/reactor
%{ruby_vendorarchdir}/types
%{ruby_vendorarchdir}/util
%else
# ...so use private install
%dir %{_libdir}/proton
%dir %{_libdir}/proton/bindings
%dir %{_libdir}/proton/bindings/ruby
%attr(755,root,root) %{_libdir}/proton/bindings/ruby/cproton.so
%{_libdir}/proton/bindings/ruby/qpid_proton.rb
%{_libdir}/proton/bindings/ruby/codec
%{_libdir}/proton/bindings/ruby/core
%{_libdir}/proton/bindings/ruby/handler
%{_libdir}/proton/bindings/ruby/reactor
%{_libdir}/proton/bindings/ruby/types
%{_libdir}/proton/bindings/ruby/util
%endif
%{_examplesdir}/ruby-%{name}-%{version}
%endif
