Name:		xgc
Version:	1.0.6
Release:	2
Summary:	X graphics demo
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	flex

%description
The xgc program demonstrates various features of the X graphics primitives.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xgc
%{_datadir}/X11/app-defaults/Xgc
%{_datadir}/X11/app-defaults/Xgc-color
%doc %{_mandir}/man1/xgc.1*
