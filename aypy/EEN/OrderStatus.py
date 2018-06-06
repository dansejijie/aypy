# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from enum import Enum

class OrderStatus(Enum):
    ORDER_STATUS_UN_DEAL="unDeal"
    ORDER_STATUS_PART_DEAL="partDeal"
    ORDER_STATUS_DEAL="deal"
    ORDER_STATUS_CANCELED="canceled"
    ORDER_STATUS_CANCELING="canceling"