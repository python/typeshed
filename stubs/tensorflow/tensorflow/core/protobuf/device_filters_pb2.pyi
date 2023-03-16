"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2020 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TaskDeviceFilters(google.protobuf.message.Message):
    """This file contains protos to be used when defining a TensorFlow
    cluster.

    Configure device filters for remote tasks in the cluster. When associated
    with a ClusterDef in setting up the cluster, a remote task will ignore all
    devices which do not match any of its filters. Device filters must be
    configured at the cluster startup, and cannot be updated once the cluster is
    up and running.

    EXAMPLES
    --------

    A two-job cluster with the following ClusterDef:

     Cluster:
       job { name: 'worker' tasks { key: 0 value: 'worker1:2222' }
                            tasks { key: 1 value: 'worker2:2222' } }
       job { name: 'ps'     tasks { key: 0 value: 'ps0:2222' }
                            tasks { key: 1 value: 'ps1:2222' } }

    Set device filters to isolate worker tasks:

     ClusterDeviceFilters:
       job { name: 'worker' tasks { key: 0
                                    value: device_filter '/job:ps'
                                           device_filter '/job:worker/task:0' }
                            tasks { key: 1
                                    value: device_filter '/job:ps'
                                           device_filter '/job:worker/task:1' } }

    Defines the device filters for a remote task.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_FILTERS_FIELD_NUMBER: builtins.int
    @property
    def device_filters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        device_filters: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["device_filters", b"device_filters"]) -> None: ...

global___TaskDeviceFilters = TaskDeviceFilters

@typing_extensions.final
class JobDeviceFilters(google.protobuf.message.Message):
    """Defines the device filters for tasks in a job."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class TasksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___TaskDeviceFilters: ...
        def __init__(
            self,
            *,
            key: builtins.int | None = ...,
            value: global___TaskDeviceFilters | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    TASKS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of this job."""
    @property
    def tasks(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___TaskDeviceFilters]:
        """Mapping from task ID to task device filters."""
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        tasks: collections.abc.Mapping[builtins.int, global___TaskDeviceFilters] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "tasks", b"tasks"]) -> None: ...

global___JobDeviceFilters = JobDeviceFilters

@typing_extensions.final
class ClusterDeviceFilters(google.protobuf.message.Message):
    """Defines the device filters for jobs in a cluster."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOBS_FIELD_NUMBER: builtins.int
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDeviceFilters]: ...
    def __init__(
        self,
        *,
        jobs: collections.abc.Iterable[global___JobDeviceFilters] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jobs", b"jobs"]) -> None: ...

global___ClusterDeviceFilters = ClusterDeviceFilters
