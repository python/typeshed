"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016 The TensorFlow Authors. All Rights Reserved.

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
import typing as typing_extensions

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class JobDef(google.protobuf.message.Message):
    """This file contains protos to be used when defining a TensorFlow
    cluster.

    EXAMPLES
    --------

    1. A single-process cluster, containing "/job:local/task:0".

       Cluster:
         job { name: 'local' tasks { key: 0 value: 'localhost:2222' } }

       Server:
         cluster { $CLUSTER } job_name: 'local' task_index: 0

    2. A two-process cluster, containing "/job:local/task:{0,1}".

       Cluster:
         job { name: 'local' tasks { key: 0 value: 'localhost:2222' }
                             tasks { key: 1 value: 'localhost:2223' } }

       Servers:
         cluster { $CLUSTER } job_name: 'local' task_index: 0
         cluster { $CLUSTER } job_name: 'local' task_index: 1

    3. A two-job cluster, containing "/job:worker/task:{0,1,2}" and
       "/job:ps/task:{0,1}".

       Cluster:
         job { name: 'worker' tasks { key: 0 value: 'worker1:2222' }
                              tasks { key: 1 value: 'worker2:2222' }
                              tasks { key: 2 value: 'worker3:2222' } }
         job { name: 'ps'     tasks { key: 0 value: 'ps0:2222' }
                              tasks { key: 1 value: 'ps1:2222' } }

       Servers:
         cluster { $CLUSTER } job_name: 'worker' task_index: 0
         cluster { $CLUSTER } job_name: 'worker' task_index: 1
         cluster { $CLUSTER } job_name: 'worker' task_index: 2
         cluster { $CLUSTER } job_name: 'ps'     task_index: 0
         cluster { $CLUSTER } job_name: 'ps'     task_index: 1

    Defines a single job in a TensorFlow cluster.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class TasksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.int | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    TASKS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of this job."""
    @property
    def tasks(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.str]:
        """Mapping from task ID to "hostname:port" string.

        If the `name` field contains "worker", and the `tasks` map contains a
        mapping from 7 to "example.org:2222", then the device prefix
        "/job:worker/task:7" will be assigned to "example.org:2222".
        """
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        tasks: collections.abc.Mapping[builtins.int, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "tasks", b"tasks"]) -> None: ...

global___JobDef = JobDef

@typing_extensions.final
class ClusterDef(google.protobuf.message.Message):
    """Defines a TensorFlow cluster as a set of jobs."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_FIELD_NUMBER: builtins.int
    @property
    def job(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JobDef]:
        """The jobs that comprise the cluster."""
    def __init__(
        self,
        *,
        job: collections.abc.Iterable[global___JobDef] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job", b"job"]) -> None: ...

global___ClusterDef = ClusterDef
