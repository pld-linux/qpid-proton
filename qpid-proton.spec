# TODO
# - bindings and bconds for them
Summary:	A high performance, lightweight messaging library
Name:		qpid-proton
Version:	0.8
Release:	0.1
License:	Apache v2.0
Group:		Libraries
Source0:	http://www.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	48bfbd7ba5a639760bb28380f4d68208
Patch0001:	0001-PROTON-731-Installing-Python-requires-Proton-be-inst.patch
URL:		http://qpid.apache.org/proton/
BuildRequires:	cmake >= 2.6
BuildRequires:	doxygen
BuildRequires:	epydoc
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	swig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	proton_datadir %{_datadir}/proton-%{version}

%description
Proton is a high performance, lightweight messaging library. It can be
used in the widest range of messaging applications including brokers,
client libraries, routers, bridges, proxies, and more. Proton is based
on the AMQP 1.0 messaging standard. Using Proton it is trivial to
integrate with the AMQP 1.0 ecosystem from any platform, environment,
or language.

%package c
Summary:	C libraries for Qpid Proton
Group:		Libraries

%description c
%{summary}.

%package c-devel
Summary:	Development libraries for writing messaging apps with Qpid Proton
Group:		Development/Libraries
Requires:	qpid-proton-c = %{version}-%{release}

%description c-devel
%{summary}.

%package c-devel-doc
Summary:	Documentation for the C development libraries for Qpid Proton
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description c-devel-doc
%{summary}.

%package -n python-%{name}
Summary:	Python language bindings for the Qpid Proton messaging framework
Group:		Libraries/Python
Requires:	%{name}-c = %{version}-%{release}

%description -n python-%{name}
%{summary}.

%package -n python-%{name}-doc
Summary:	Documentation for the Python language bindings for Qpid Proton
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n python-%{name}-doc
%{summary}.

%prep
%setup -q
%patch0001 -p1

%build
%cmake \
	-DPROTON_DISABLE_RPATH=true \
	-DPYTHON_SITEARCH_PACKAGES=%{python_sitearch} \
	-DBINDING_LANGS="%{?with_perl:PERL} %{?with_php:PHP} %{?with_python:PYTHON} %{?with_ruby:RUBY}" \
	-DNOBUILD_RUBY=1 \
	-DNOBUILD_PHP=1 \
	-DNOBUILD_JAVA=1 \
	-DBUILD_PYTHON=0 \
	-DBUILD_PERL=0 \
	-DSYSINSTALL_PYTHON=1 \
	-DSYSINSTALL_PERL=0 \
	-DCHECK_SYSINSTALL_PYTHON=0 \
	.

%{__make} all docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
chmod +x $RPM_BUILD_ROOT%{py_sitedir}/_cproton.so
%endif

# clean up files that are not shipped
rm -rf $RPM_BUILD_ROOT%{_exec_prefix}/bindings
rm -rf $RPM_BUILD_ROOT%{_libdir}/java
rm -rf $RPM_BUILD_ROOT%{_libdir}/libproton-jni.so
rm -rf $RPM_BUILD_ROOT%{_datarootdir}/java
rm -rf $RPM_BUILD_ROOT%{_libdir}/proton.cmake

%clean
rm -rf $RPM_BUILD_ROOT

%post	c -p /sbin/ldconfig
%postun	c -p /sbin/ldconfig

%files c
%defattr(644,root,root,755)
%dir %{proton_datadir}
%doc %{proton_datadir}/LICENSE
%doc %{proton_datadir}/README
%doc %{proton_datadir}/TODO
%attr(755,root,root) %{_libdir}/libqpid-proton.so.*.*.*
%ghost %{_libdir}/libqpid-proton.so.2
%attr(755,root,root) %{_bindir}/proton
%attr(755,root,root) %{_bindir}/proton-dump
%{_mandir}/man1/proton-dump.1*
%{_mandir}/man1/proton.1*

%files c-devel
%defattr(644,root,root,755)
%{_includedir}/proton
%{_libdir}/libqpid-proton.so
%{_pkgconfigdir}/libqpid-proton.pc
%{_libdir}/cmake/Proton
%{_datadir}/proton/examples

%files c-devel-doc
%defattr(644,root,root,755)
%doc %{proton_datadir}/docs/api-c

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitedir}/_cproton.so
%{py_sitedir}/cproton.*
%{py_sitedir}/proton.*

%files -n python-%{name}-doc
%defattr(644,root,root,755)
%doc %{proton_datadir}/docs/api-py
%endif
