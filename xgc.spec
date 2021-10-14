Name:		xgc
Version:	1.0.5
Release:	4
Summary:	X graphics demo
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	flex

%description
The xgc program demonstrates various features of the X graphics primitives.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xgc
%{_datadir}/X11/app-defaults/Xgc
%{_datadir}/X11/app-defaults/Xgc-color
%{_mandir}/man1/xgc.1*
