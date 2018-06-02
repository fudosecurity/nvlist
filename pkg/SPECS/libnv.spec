%define version	%(cat %{_topdir}/version.txt)

Name:		libnv
Version:	%{version}
Release:	1%{?dist}
Summary:	FreeBSD's name/value pairs library
Group:		System Environment/Libraries
License:	BSD
URL:		https://github.com/wheelsystems/nvlist
Source0:	libnv.tar.gz

BuildRequires:	make
BuildRequires:	libtool

%description
The libnv library is a general purpose name/value pairs mechanism used
in FreeBSD, which was inspired by the nvpairs used in Solaris/illumos.
It is a lightweight serialization (marshalling) library.

%prep
%setup -q -n src

%build
make %{?_smp_mflags} LIBDIR=%{_libdir}

%install
make install \
    DESTDIR=%{buildroot} \
    LIBDIR=%{_libdir} \
    INCDIR=%{_includedir} \
    MANDIR=%{_mandir}

%files
%{_libdir}/*
%{_includedir}/*
%{_mandir}/*

%changelog
