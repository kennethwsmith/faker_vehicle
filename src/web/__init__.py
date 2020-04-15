# -*- coding: utf-8 -*-
from faker.providers import BaseProvider

from .mimetypes import mime_types


class WebProvider(BaseProvider):
    """
    A Provider for vehicle related test data.

    >>> from faker import Faker
    >>> from faker_vehicle import WebProvider
    >>> fake = Faker()
    >>> fake.add_provider(WebProvider)
    """
    all_mime_types = mime_types

    popular_mime_types = {
        'application/javascript': ['js'],
        'application/json': ['json'],
        'application/pdf': ['pdf'],
        'image/jpeg': ['jpeg', 'jpg', 'jpe'],
        'image/gif': ['gif'],
        'image/png': ['png'],
        'image/svg+xml': ['svg', 'svgz'],
        'text/css': ['css'],
        'text/html': ['html', 'htm'],
        'text/plain': ['txt', 'text', 'conf', 'def', 'list', 'log', 'in'],
    }

    web_servers = (
        'apache',
        'nginx',
        'iis',
        'varnish',
    )

    apache_versions = {
        '1.3': list(range(1, 42)),
        '2.0': list(range(35, 65)),
        '2.2': list(range(0, 32)),
        '2.4': list(range(1, 25)),
    }

    apache_distro = (
        'Amazon',
        'CentOS',
        'Debian',
        'Fedora',
        'Red Hat',
        'Ubuntu',
        'Unix',
    )

    nginx_versions = {
        '1.4': list(range(0, 7)),
        '1.5': list(range(0, 13)),
        '1.6': list(range(0, 3)),
        '1.7': list(range(0, 10)),
        '1.8': list(range(0, 1)),
        '1.9': list(range(0, 15)),
        '1.10': list(range(0, 3)),
        '1.11': list(range(0, 8)),
        '1.12': list(range(0, 0)),
    }

    iis_versions = (
        '1.0',
        '2.0',
        '3.0',
        '4.0',
        '5.0',
        '5.1',
        '6.0',
        '7.0',
        '7.5',
        '8.0',
    )

    def content_type(self):
        """
        Returns a mime-type from the list of types understood by the Apache
        http server.

        >>> fake.content_type()
        application/mxf

        :return: content-type
        :rtype: str
        """
        return self.random_element(self.all_mime_types.keys())

    def content_type_popular(self):
        """
        Returns a popular mime-type.

        >>> fake.content_type_popular()
        text/html

        :return: content-type/mime-type
        :rtype: str
        """
        return self.random_element(self.popular_mime_types.keys())

    def _web_server_version(self, choices):
        minor = self.random_element(choices.keys())
        patch = self.random_element(choices.get(minor))
        return '{minor}.{patch}'.format(**locals())

    def apache(self):
        version = self._web_server_version(self.apache_versions)
        os = self.random_element(self.apache_distro)
        return 'Apache/{version} ({os})'.format(**locals())

    def nginx(self):
        version = self._web_server_version(self.apache_versions)
        return 'nginx/' + version

    def iis(self):
        return 'Microsoft-IIS/' + self.random_element(self.iis_versions)

    def varnish(self):
        return 'Varnish'

    def server_token(self):
        """
        Returns a http web server response header, as per RFC-2616, section
        14.38
        https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.38

        >>> fake.server_token()
        Apache/2.4.9 (Unix)

        :return: web server signature.
        :rtype: str
        """
        return getattr(self, self.random_element(self.web_servers))()
