%{!?python_sitearch: %global python_sitearch %([ -x %{__python} ] && %{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)" || :)}

Name:           python-cheetah
Version:        2.4.1
Release:        1%{?dist}
Summary:        Template engine and code generator

Group:          Development/Libraries
License:        MIT
URL:            http://cheetahtemplate.org/
Source:         http://pypi.python.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python-markdown
BuildRequires: python-pygments

Requires: python-markdown
Requires: python-pygments

%description
Cheetah is an open source template engine and code generation tool,
written in Python. It can be used standalone or combined with other
tools and frameworks. Web development is its principle use, but
Cheetah is very flexible and is also being used to generate C++ game
code, Java, sql, form emails and even Python code.

%prep
%setup -q -n Cheetah-%{version}
# remove shebangs
%{__sed} -i -e '/^#!/,1d' cheetah/Tests/* \
    cheetah/DirectiveAnalyzer.py cheetah/Utils/Misc.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
export PATH="%{buildroot}/%{_bindir}:$PATH"
export PYTHONPATH="%{buildroot}/%{python_sitearch}"
%{__python} %{buildroot}/%{python_sitearch}/Cheetah/Tests/Test.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.markdown TODO

%{_bindir}/cheetah
%{_bindir}/cheetah-analyze
%{_bindir}/cheetah-compile

%dir %{python_sitearch}/Cheetah
%{python_sitearch}/Cheetah/*.py*
%{python_sitearch}/Cheetah/_namemapper.so

%dir %{python_sitearch}/Cheetah/Macros
%{python_sitearch}/Cheetah/Macros/*.py*

%dir %{python_sitearch}/Cheetah/Templates
%{python_sitearch}/Cheetah/Templates/*.py*
%{python_sitearch}/Cheetah/Templates/*.tmpl

%dir %{python_sitearch}/Cheetah/Tests
%{python_sitearch}/Cheetah/Tests/*.py*

%dir %{python_sitearch}/Cheetah/Tools
%{python_sitearch}/Cheetah/Tools/*.py*
%{python_sitearch}/Cheetah/Tools/*.txt

%dir %{python_sitearch}/Cheetah/Utils
%{python_sitearch}/Cheetah/Utils/*.py*

%dir %{python_sitearch}/Cheetah-%{version}-*.egg-info
%{python_sitearch}/Cheetah-%{version}-*.egg-info/PKG-INFO
%{python_sitearch}/Cheetah-%{version}-*.egg-info/*.txt

%changelog
* Fri Jan 15 2010 Radek Novacek <rnovacek@redhat.com> - 2.4.1-1
- Update to version 2.4.1

* Wed Jan 13 2010 Radek Novacek <rnovacek@redhat.com> - 2.2.2-3
- Fixed source url
- Add patch comment
- Removed shebang lines from non-executable files

* Tue Oct 20 2009 Mike Bonnet <mikeb@redhat.com> - 2.2.2-2
- backport significant improvements to utf-8/unicode handling from upstream

* Mon Sep 14 2009 Mike Bonnet <mikeb@redhat.com> - 2.2.2-1
- update to the 2.2.2 release
- add dependency on python-markdown for consistency with the egg-info

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Mike Bonnet <mikeb@redhat.com> - 2.2.1-1
- update to the 2.2.1 release

* Mon May 18 2009 Mike Bonnet <mikeb@redhat.com> - 2.2.0-1
- update to the 2.2.0 release
- remove unneeded importHook() patch, it has been included upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.1-4
- Fix cheetah enough that it will pass its unittests on python-2.6.  This has
  actually been broken since py-2.5 and this fix is only a workaround.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.1-3
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.1-2
- Autorebuild for GCC 4.3

* Tue Dec  4 2007 Mike Bonnet <mikeb@redhat.com> - 2.0.1-1
- update to the 2.0.1 release

* Mon Oct 15 2007 Mike Bonnet <mikeb@redhat.com> - 2.0-1
- update to the 2.0 release

* Tue Aug 21 2007 Mike Bonnet <mikeb@redhat.com> - 2.0-0.7.rc8
- rebuild for F8

* Thu May  3 2007 Mike Bonnet <mikeb@redhat.com> - 2.0-0.6.rc8
- bump release for rebuild

* Mon Apr 23 2007 Mike Bonnet <mikeb@redhat.com> - 2.0-0.5.rc8
- update to 2.0rc8

* Mon Jan  8 2007 Mike Bonnet <mikeb@redhat.com> - 2.0-0.4.rc7
- use setuptools and install setuptools metadata

* Sun Dec 10 2006 Mike Bonnet <mikeb@redhat.com> - 2.0-0.3.rc7
- rebuild against python 2.5
- remove obsolete python-abi Requires:

* Mon Sep 11 2006 Mike Bonnet <mikeb@redhat.com> - 2.0-0.2.rc7
- un-%%ghost .pyo files

* Thu Jul 13 2006 Mike Bonnet <mikeb@redhat.com> - 2.0-0.1.rc7
- update to 2.0rc7
- change %%release format to conform to Extras packaging guidelines

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 2.0-0.rc6.0
- update to 2.0rc6
- run the included test suite after install

* Thu Feb 16 2006 Mike Bonnet <mikeb@redhat.com> - 1.0-2
- Rebuild for Fedora Extras 5

* Wed Dec  7 2005 Mike Bonnet <mikeb@redhat.com> - 1.0-1
- Initial version
