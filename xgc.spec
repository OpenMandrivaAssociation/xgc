Name:		xgc
Version:	1.0.3
Release:	%mkrel 2
Summary:	X graphics demo
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires:	flex

%description
The xgc program demonstrates various features of the X graphics primitives.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xgc
%{_datadir}/X11/app-defaults/Xgc
%{_datadir}/X11/app-defaults/Xgc-color
%{_mandir}/man1/xgc.1*
