# django-swap-user

# архитектура
приложение swap_user засплитовано на еще 2 приложения:
  - email
  - named_email
  
потому что, если оставить их в одном аппе - то они вдвоем создают миграции и таблицы.
если их оставить, они будут считаться как 2 кастомные модели в пределах одного приложения, что вызывает
недоумение и когнитивную нагрузку.

при такой архитектуре (когда есть общий апп, который содержит внутренние аппы) - пользователь
подключает только ту кастомную модель юзера, которая ему больше подходит.