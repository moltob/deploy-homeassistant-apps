from datetime import datetime
from typing import Any, Literal

from .pyscript_builtins import StateVal


class assist_satellite:
    @staticmethod
    def announce(
        *,
        entity_id: str,
        message: str = '',
        media_id=None,
        preannounce: bool = True,
        preannounce_media_id=None,
    ):
        """

        Args:
            entity_id: Entity ID
            message:  Example: Time to wake up!"""
        ...

    @staticmethod
    def start_conversation(
        *,
        entity_id: str,
        start_message: str = '',
        start_media_id=None,
        extra_system_prompt: str | None = None,
        preannounce: bool = True,
        preannounce_media_id=None,
    ):
        """

        Args:
            entity_id: Entity ID
            start_message:  Example: You left the lights on in the living room. Turn them off?"""
        ...

    @staticmethod
    def ask_question(
        *,
        entity_id: str,
        question: str = '',
        question_media_id=None,
        preannounce: bool = True,
        preannounce_media_id=None,
        answers: Any | None = None,
    ) -> dict[str, Any]:
        """

        Args:
            question:  Example: What kind of music would you like to play?"""
        ...


class _automation_state(StateVal):
    current: int
    id: str
    last_triggered: datetime
    mode: str

    def trigger(self, skip_condition: bool): ...

    def toggle(self): ...

    def turn_on(self): ...

    def turn_off(self, stop_actions: bool): ...


class automation:
    gardenlights: _automation_state
    update_ha_ipv6_strato: _automation_state
    wasseruberwachung_keller: _automation_state
    kaffeemaschine_an_per_timer: _automation_state
    kaffeemaschine_ein_aus: _automation_state

    @staticmethod
    def trigger(*, entity_id: str, skip_condition: bool = True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str, stop_actions: bool = True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def reload(): ...


class backup:
    @staticmethod
    def create_automatic(): ...


class _binary_sensor_state(StateVal):
    restored: bool
    supported_features: int


class binary_sensor:
    rpi_power_status: _binary_sensor_state
    laundry_washer_overpowering: _binary_sensor_state
    laundry_dryer_overpowering: _binary_sensor_state
    shelly1l_98cdac2e60bd_overheating: _binary_sensor_state
    guestbath_lamp_overheating: _binary_sensor_state
    remote_ui: _binary_sensor_state
    attic_radiator_tastensperre_am_gerat: _binary_sensor_state
    attic_radiator_tastensperre_uber_ui: _binary_sensor_state
    router_connection: _binary_sensor_state
    internet_connection: _binary_sensor_state
    iphone_von_ben_focus: _binary_sensor_state
    ben_pagel_focus: _binary_sensor_state
    zigbee2mqtt_bridge_connection_state: _binary_sensor_state
    first_floor_light_overheating: _binary_sensor_state
    ground_floor_light_overheating: _binary_sensor_state
    first_floor_light_overpowering: _binary_sensor_state
    ground_floor_light_overpowering: _binary_sensor_state
    first_floor_light_overvoltage: _binary_sensor_state
    ground_floor_light_overvoltage: _binary_sensor_state
    shelly_flood_12_flood: _binary_sensor_state
    shelly_flood_11_flood: _binary_sensor_state
    shelly_flood_10_flood: _binary_sensor_state
    coffeemaker_overheating: _binary_sensor_state
    coffeemaker_overpowering: _binary_sensor_state
    zigbee2mqtt_bridge_connection_state_2: _binary_sensor_state
    attic_window_2_contact: _binary_sensor_state
    galaxy_tab_a7_kioskmodus: _binary_sensor_state
    galaxy_tab_a7_eingesteckt: _binary_sensor_state
    galaxy_tab_a7_gerateadministrator: _binary_sensor_state
    first_floor_light_overcurrent: _binary_sensor_state
    ground_floor_light_overcurrent: _binary_sensor_state
    guestbath_radiator_battery_low: _binary_sensor_state
    bedroom_ben_radiator_setup: _binary_sensor_state
    bedroom_ben_radiator_calibrated: _binary_sensor_state
    bedroom_ben_radiator_window_open: _binary_sensor_state
    bedroom_ben_radiator_valve_alarm: _binary_sensor_state
    bedroom_ben_window_contact: _binary_sensor_state
    guestbath_window_contact: _binary_sensor_state
    attic_radiator_urlaubsmodus: _binary_sensor_state
    attic_radiator_sommermodus: _binary_sensor_state
    attic_radiator_offenes_fenster_erkannt: _binary_sensor_state
    attic_window_contact: _binary_sensor_state
    attic_window_battery_low: _binary_sensor_state


class blueprint: ...


class _button_state(StateVal):
    restored: bool
    supported_features: int

    def press(self): ...


class button:
    laundry_washer_reboot: _button_state
    laundry_dryer_reboot: _button_state
    shelly_plug_02_reboot: _button_state
    shelly1l_98cdac2e60bd_reboot: _button_state
    office_mike_light_reboot: _button_state
    guestbath_lamp_reboot: _button_state
    shelly_pro2pm_06_reboot: _button_state
    coffeemaker_reboot: _button_state
    zigbee2mqtt_bridge_restart: _button_state
    homeassistant_restart: _button_state
    homeassistant_reload: _button_state
    ignore_all_issues: _button_state
    unignore_all_issues: _button_state
    galaxy_tab_a7_browser_neustarten: _button_state
    galaxy_tab_a7_gerat_neustarten: _button_state
    galaxy_tab_a7_in_den_vordergrund_rucken: _button_state
    galaxy_tab_a7_in_den_hintergrund_rucken: _button_state
    galaxy_tab_a7_start_url_laden: _button_state
    m5stack_atom_echo_0dbb0c_safe_mode_boot: _button_state
    m5stack_atom_echo_0dbb0c_factory_reset: _button_state
    bedroom_ben_radiator_calibrate: _button_state
    galaxy_tab_a7_browser_cache_leeren: _button_state

    @staticmethod
    def press(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class _camera_state(StateVal):
    access_token: str
    entity_picture: str
    supported_features: int

    def enable_motion_detection(self): ...

    def disable_motion_detection(self): ...

    def turn_off(self): ...

    def turn_on(self): ...

    def snapshot(self, filename: str):
        """

        Args:
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.jpg"""
        ...

    def play_stream(self, *, media_player: str, format: Literal['', 'hls'] = 'hls'): ...

    def record(self, *, filename: str, duration: int = 30, lookback: int = 0):
        """

        Args:
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.mp4"""
        ...


class camera:
    galaxy_tab_a7: _camera_state

    @staticmethod
    def enable_motion_detection(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def disable_motion_detection(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def snapshot(*, entity_id: str, filename: str):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.jpg"""
        ...

    @staticmethod
    def play_stream(*, entity_id: str, media_player: str, format: Literal['', 'hls'] = 'hls'):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def record(*, entity_id: str, filename: str, duration: int = 30, lookback: int = 0):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.mp4"""
        ...


class _climate_state(StateVal):
    current_temperature: float
    hvac_modes: list
    max_temp: float
    min_temp: float
    preset_mode: str
    preset_modes: list
    supported_features: int
    target_temp_step: float
    temperature: float

    def turn_on(self): ...

    def turn_off(self): ...

    def toggle(self): ...

    def set_hvac_mode(self, hvac_mode: str | None): ...

    def set_preset_mode(self, preset_mode: str):
        """

        Args:
            preset_mode:  Example: away"""
        ...

    def set_temperature(
        self,
        *,
        temperature: float | None = None,
        target_temp_high: float | None = None,
        target_temp_low: float | None = None,
        hvac_mode: Literal['', 'off', 'auto', 'cool', 'dry', 'fan_only', 'heat_cool', 'heat']
        | None = None,
    ): ...

    def set_humidity(self, humidity: int): ...

    def set_fan_mode(self, fan_mode: str):
        """

        Args:
            fan_mode:  Example: low"""
        ...

    def set_swing_mode(self, swing_mode: str):
        """

        Args:
            swing_mode:  Example: on"""
        ...

    def set_swing_horizontal_mode(self, swing_horizontal_mode: str):
        """

        Args:
            swing_horizontal_mode:  Example: on"""
        ...


class climate:
    attic_radiator: _climate_state
    guestbath_radiator: _climate_state
    bedroom_ben_radiator: _climate_state

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_hvac_mode(*, entity_id: str, hvac_mode: str | None = None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_preset_mode(*, entity_id: str, preset_mode: str):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: away"""
        ...

    @staticmethod
    def set_temperature(
        *,
        entity_id: str,
        temperature: float | None = None,
        target_temp_high: float | None = None,
        target_temp_low: float | None = None,
        hvac_mode: Literal['', 'off', 'auto', 'cool', 'dry', 'fan_only', 'heat_cool', 'heat']
        | None = None,
    ):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_humidity(*, entity_id: str, humidity: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_fan_mode(*, entity_id: str, fan_mode: str):
        """

        Args:
            entity_id: Entity ID
            fan_mode:  Example: low"""
        ...

    @staticmethod
    def set_swing_mode(*, entity_id: str, swing_mode: str):
        """

        Args:
            entity_id: Entity ID
            swing_mode:  Example: on"""
        ...

    @staticmethod
    def set_swing_horizontal_mode(*, entity_id: str, swing_horizontal_mode: str):
        """

        Args:
            entity_id: Entity ID
            swing_horizontal_mode:  Example: on"""
        ...


class cloud:
    @staticmethod
    def remote_connect(): ...

    @staticmethod
    def remote_disconnect(): ...


class command_line:
    @staticmethod
    def reload(): ...


class conversation:
    @staticmethod
    def process(
        *, text: str, language: str | None = None, agent_id=None, conversation_id: str | None = None
    ) -> dict[str, Any]:
        """

        Args:
            text:  Example: Turn all lights on
            language:  Example: NL
            agent_id:  Example: homeassistant
            conversation_id:  Example: my_conversation_1"""
        ...

    @staticmethod
    def reload(*, language: str | None = None, agent_id=None):
        """

        Args:
            language:  Example: NL
            agent_id:  Example: homeassistant"""
        ...


class counter:
    @staticmethod
    def increment(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrement(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def reset(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """

        Args:
            entity_id: Entity ID"""
        ...


class cover:
    @staticmethod
    def open_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_cover_position(*, entity_id: str, position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def open_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_cover_tilt_position(*, entity_id: str, tilt_position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class _device_tracker_state(StateVal):
    altitude: float
    battery_level: int
    course: int
    gps_accuracy: int
    latitude: float
    longitude: float
    source_type: str
    speed: int
    vertical_accuracy: float | int


class device_tracker:
    s22_mike: _device_tracker_state
    s21fe_britta: _device_tracker_state
    iphone_von_ben: _device_tracker_state
    ben_pagel: _device_tracker_state
    public_tablet: _device_tracker_state

    @staticmethod
    def see(
        *,
        mac: str | None = None,
        dev_id: str | None = None,
        host_name: str | None = None,
        location_name: str | None = None,
        gps: Any | None = None,
        gps_accuracy: float | None = None,
        battery: int | None = None,
    ):
        """

        Args:
            mac:  Example: FF:FF:FF:FF:FF:FF
            dev_id:  Example: phonedave
            host_name:  Example: Dave
            location_name:  Example: home
            gps:  Example: [51.509802, -0.086692]"""
        ...


class _event_state(StateVal):
    backup_stage: Any
    domain: str
    event_type: str
    event_types: list
    failed_reason: Any
    issue_id: str


class event:
    shelly_1l_04_channel_1: _event_state
    shelly1l_98cdac2f3642_channel_1: _event_state
    shelly_pro2pm_06_input_0: _event_state
    shelly_pro2pm_06_input_1: _event_state
    repair: _event_state
    backup_automatisches_backup: _event_state


class fan:
    @staticmethod
    def turn_on(*, entity_id: str, percentage: int | None = None, preset_mode: str | None = None):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: auto"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def increase_speed(*, entity_id: str, percentage_step: int | None = None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrease_speed(*, entity_id: str, percentage_step: int | None = None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def oscillate(*, entity_id: str, oscillating: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_direction(*, entity_id: str, direction: Literal['', 'forward', 'reverse']):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_percentage(*, entity_id: str, percentage: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_preset_mode(*, entity_id: str, preset_mode: str):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: auto"""
        ...


class ffmpeg:
    @staticmethod
    def start(*, entity_id: str | None = None): ...

    @staticmethod
    def stop(*, entity_id: str | None = None): ...

    @staticmethod
    def restart(*, entity_id: str | None = None): ...


class file:
    @staticmethod
    def read_file(
        *, file_name: str | None = None, file_encoding: Literal['', 'JSON', 'YAML'] | None = None
    ) -> dict[str, Any]:
        """

        Args:
            file_name:  Example: www/my_file.json
            file_encoding:  Example: JSON"""
        ...


class frontend:
    @staticmethod
    def set_theme(*, name, mode: Literal['', 'dark', 'light'] = 'light'):
        """

        Args:
            name:  Example: default"""
        ...

    @staticmethod
    def reload_themes(): ...


class fully_kiosk:
    @staticmethod
    def load_url(*, device_id, url: str):
        """

        Args:
            url:  Example: https://home-assistant.io"""
        ...

    @staticmethod
    def start_application(*, application: str, device_id):
        """

        Args:
            application:  Example: de.ozerov.fully"""
        ...

    @staticmethod
    def set_config(*, device_id, key: str, value: str):
        """

        Args:
            key:  Example: motionSensitivity
            value:  Example: 90"""
        ...


class group:
    @staticmethod
    def reload(): ...

    @staticmethod
    def set(
        *,
        object_id: str,
        name: str | None = None,
        icon: str | None = None,
        entities: str | None = None,
        add_entities: str | None = None,
        remove_entities: str | None = None,
        all: bool | None = None,
    ):
        """

        Args:
            object_id:  Example: test_group
            name:  Example: My test group
            icon:  Example: mdi:camera
            entities:  Example: domain.entity_id1, domain.entity_id2
            add_entities:  Example: domain.entity_id1, domain.entity_id2
            remove_entities:  Example: domain.entity_id1, domain.entity_id2"""
        ...

    @staticmethod
    def remove(*, object_id: Any):
        """

        Args:
            object_id:  Example: test_group"""
        ...


class hassio:
    @staticmethod
    def addon_start(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def addon_stop(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def addon_restart(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def addon_stdin(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def host_shutdown(): ...

    @staticmethod
    def host_reboot(): ...

    @staticmethod
    def backup_full(
        *,
        name: str | None = None,
        password: str | None = None,
        compressed: bool = True,
        location=None,
        homeassistant_exclude_database: bool = False,
    ):
        """

        Args:
            name:  Example: Backup 1
            password:  Example: password
            location:  Example: my_backup_mount"""
        ...

    @staticmethod
    def backup_partial(
        *,
        homeassistant: bool | None = None,
        homeassistant_exclude_database: bool = False,
        addons: Any | None = None,
        folders: Any | None = None,
        name: str | None = None,
        password: str | None = None,
        compressed: bool = True,
        location=None,
    ):
        """

        Args:
            addons:  Example: ['core_ssh', 'core_samba', 'core_mosquitto']
            folders:  Example: ['homeassistant', 'share']
            name:  Example: Partial backup 1
            password:  Example: password
            location:  Example: my_backup_mount"""
        ...

    @staticmethod
    def restore_full(*, slug: str, password: str | None = None):
        """

        Args:
            password:  Example: password"""
        ...

    @staticmethod
    def restore_partial(
        *,
        slug: str,
        homeassistant: bool | None = None,
        folders: Any | None = None,
        addons: Any | None = None,
        password: str | None = None,
    ):
        """

        Args:
            folders:  Example: ['homeassistant', 'share']
            addons:  Example: ['core_ssh', 'core_samba', 'core_mosquitto']
            password:  Example: password"""
        ...


class homeassistant:
    @staticmethod
    def save_persistent_states(): ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop(): ...

    @staticmethod
    def check_config(): ...

    @staticmethod
    def update_entity(*, entity_id: str): ...

    @staticmethod
    def reload_core_config(): ...

    @staticmethod
    def set_location(*, latitude: float, longitude: float, elevation: float | None = None):
        """

        Args:
            latitude:  Example: 32.87336
            longitude:  Example: 117.22743
            elevation:  Example: 120"""
        ...

    @staticmethod
    def reload_custom_templates(): ...

    @staticmethod
    def reload_config_entry(*, entity_id: str, entry_id: str | None = None):
        """

        Args:
            entity_id: Entity ID
            entry_id:  Example: 8955375327824e14ba89e4b29cc3ec9a"""
        ...

    @staticmethod
    def reload_all(): ...

    @staticmethod
    def remove_label_from_entity(*, label_id, entity_id: str):
        """Removes a label from an entity. If multiple labels or multiple entities are provided, all combinations will be removed.

        Args:
            label_id: The ID(s) of the label(s) to remove from the entity/entities.
            entity_id: The ID(s) of the entity/entities to remove the label(s) from."""
        ...

    @staticmethod
    def add_label_to_entity(*, label_id, entity_id: str):
        """Adds a label to an entity. If multiple labels or multiple entities are provided, all combinations will be added.

        Args:
            label_id: The ID(s) of the label(s) to add the entity/entities.
            entity_id: The ID(s) of the entity/entities to add the label(s) to."""
        ...

    @staticmethod
    def remove_alias_from_area(*, area_id, alias: Any):
        """Removes an alias from an area.

        Args:
            area_id: The ID of the area to remove the alias from.
            alias: The alias (or list of aliasses) to remove from the area."""
        ...

    @staticmethod
    def enable_entity(*, entity_id: str):
        """Enables an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to enable."""
        ...

    @staticmethod
    def remove_device_from_area(*, device_id):
        """Removes a device from an area. As a device can only be in one area, this call doesn't need to specify the area.

        Args:
            device_id: The ID of the device to remove the area from."""
        ...

    @staticmethod
    def disable_device(*, device_id):
        """Disables a device on the fly.

        Args:
            device_id: The device(s) to disable."""
        ...

    @staticmethod
    def add_device_to_area(*, area_id, device_id):
        """Adds an device to an area. Please note, if the device is already in an area, it will be removed from the previous area.

        Args:
            area_id: The ID of the area to add the device to.
            device_id: The ID of the device(s) to add to the area."""
        ...

    @staticmethod
    def add_label_to_area(*, label_id, area_id):
        """Adds a label to an area. If multiple labels or multiple areas are provided, all combinations will be added.

        Args:
            label_id: The ID(s) of the label(s) to add the area(s).
            area_id: The ID(s) of the area(s) to add the label(s) to."""
        ...

    @staticmethod
    def remove_entity_from_area(*, entity_id: str):
        """Removes an entity from an area. As an entity can only be in one area, this call doesn't need to specify the area. Please note, the entity will still be in the area of the device that provides it after this call.

        Args:
            entity_id: The ID of the entity (or entities) to remove the area from."""
        ...

    @staticmethod
    def remove_area_from_floor(*, area_id):
        """Removes an area from a floor. As an area can only be on one floor, this call doesn't need to specify the floor.

        Args:
            area_id: The ID of the area to remove the floor from."""
        ...

    @staticmethod
    def hide_entity(*, entity_id: str):
        """Hides an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to hide."""
        ...

    @staticmethod
    def remove_label_from_area(*, label_id, area_id):
        """Removes a label to an area. If multiple labels or multiple areas are provided, all combinations will be removed.

        Args:
            label_id: The ID(s) of the label(s) to remove from the area(s).
            area_id: The ID(s) of the area(s) to remove the label(s) from."""
        ...

    @staticmethod
    def remove_alias_from_floor(*, floor_id, alias: Any):
        """Removes an alias from a floor.

        Args:
            floor_id: The ID of the floor to remove the alias from.
            alias: The alias (or list of aliasses) to remove from the floor."""
        ...

    @staticmethod
    def remove_label_from_device(*, label_id, device_id):
        """Removes a label from a device. If multiple labels or multiple devices are provided, all combinations will be removed.

        Args:
            label_id: The ID(s) of the label(s) to remove from the device(s).
            device_id: The ID(s) of the device(s) to remove the label(s) from."""
        ...

    @staticmethod
    def ignore_all_discovered(*, domain: str | None = None):
        """Ignore all currently discovered devices that are shown on the integrations dashboard. This will not ignore devices that are discovered after this.

        Args:
            domain: The integration domain to ignore all discovered devices for. If not provided, all domains will be considered to be ignored."""
        ...

    @staticmethod
    def add_area_to_floor(*, floor_id, area_id):
        """Adds an area to a floor. Please note, if the area is already on a floor, it will be removed from the previous floor.

        Args:
            floor_id: The ID of the floor to add the area on.
            area_id: The ID of the area(s) to add to the floor."""
        ...

    @staticmethod
    def enable_device(*, device_id):
        """Enables a device on the fly.

        Args:
            device_id: The device(s) to enable."""
        ...

    @staticmethod
    def disable_entity(*, entity_id: str):
        """Disables an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to disable."""
        ...

    @staticmethod
    def enable_config_entry(*, config_entry_id: str):
        """Enables an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to enable."""
        ...

    @staticmethod
    def disable_polling(*, config_entry_id: str):
        """Disables polling for updates for an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to disable polling for."""
        ...

    @staticmethod
    def delete_floor(*, floor_id):
        """Deletes a floor on the fly.

        Args:
            floor_id: The ID of the floor to delete."""
        ...

    @staticmethod
    def add_alias_to_floor(*, floor_id, alias: Any):
        """Adds an alias to a floor.

        Args:
            floor_id: The ID of the floor to add the alias to.
            alias: The alias (or list of aliasses) to add to the floor."""
        ...

    @staticmethod
    def create_label(
        *,
        name: str,
        description: str,
        icon: str | None = None,
        color: Literal[
            '',
            'primary',
            'accent',
            'disabled',
            'red',
            'pink',
            'purple',
            'deep_purple',
            'indigo',
            'blue',
            'light_blue',
            'cyan',
            'teal',
            'green',
            'light_green',
            'lime',
            'yellow',
            'orange',
            'deep_orange',
            'brown',
            'grey',
            'blue_grey',
            'black',
            'white',
        ]
        | None = None,
    ):
        """Creates a new label on the fly.

        Args:
            name: The name of the label to create.
            description: Description for the label.
            icon: Icon to use for the label.
            color: Color to use for the label. Can be a color name from the list, or a hex color code (like #FF0000)."""
        ...

    @staticmethod
    def create_floor(
        *,
        name: str,
        icon: str | None = None,
        level: float | None = None,
        aliases: Any | None = None,
    ):
        """Creates a new floor on the fly.

        Args:
            name: The name of the floor to create.
            icon: Icon to use for the floor.
            level: The level the floor is on in your home.
            aliases: A list of aliases for the floor. This is useful if you want to use the floor in a different language or different nickname."""
        ...

    @staticmethod
    def restart(*, safe_mode: bool | None = None, force: bool | None = None):
        """Restart the Home Assistant action.

        Args:
            safe_mode: If the restart should be done in safe mode. This will disable all custom integrations and frontend modules.
            force: Force the restart. WARNING! This will not gracefully shutdown Home Assistant, it will skip configuration checks and ignore running database migrations. Only use this if you know what you are doing."""
        ...

    @staticmethod
    def update_entity_id(*, entity_id: str, new_entity_id: str):
        """Updates an entity's ID on the fly.

        Args:
            entity_id: The entity/entities to update.
            new_entity_id: The new ID for the entity"""
        ...

    @staticmethod
    def list_orphaned_database_entities() -> dict[str, Any]:
        """Lists all orphaned database entities unclaimed by any integration."""
        ...

    @staticmethod
    def unhide_entity(*, entity_id: str):
        """Unhides an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to unhide."""
        ...

    @staticmethod
    def delete_area(*, area_id):
        """Deletes a new area on the fly.

        Args:
            area_id: The ID of the area to delete."""
        ...

    @staticmethod
    def disable_config_entry(*, config_entry_id: str):
        """Disables an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to disable."""
        ...

    @staticmethod
    def add_alias_to_area(*, area_id, alias: Any):
        """Adds an alias to an area.

        Args:
            area_id: The ID of the area to add the alias to.
            alias: The alias (or list of aliasses) to add to the area."""
        ...

    @staticmethod
    def delete_label(*, label_id):
        """Deletes a label on the fly.

        Args:
            label_id: The ID of the label to delete."""
        ...

    @staticmethod
    def enable_polling(*, config_entry_id: str):
        """Enables polling for updates for an integration configuration entry.

        Args:
            config_entry_id: The integration configuration entry to enable polling for."""
        ...

    @staticmethod
    def set_floor_aliases(*, floor_id, aliases: Any):
        """Sets aliases for a floor. Overwrite and removed any existing aliases, fully replacing them with the new ones.

        Args:
            floor_id: The ID of the floor to set the aliases for.
            aliases: The aliases to set for the floor."""
        ...

    @staticmethod
    def delete_all_orphaned_entities():
        """Deletes all orphaned entities that no longer have an integration that claim/provide them. Please note, if the integration was just removed, it might need a restart for Home Assistant to realize they are orphaned.
        **WARNING** Entities might have been marked orphaned because an integration is offline or not working since Home Assistant started. Calling this action will delete those entities as well."""
        ...

    @staticmethod
    def rename_entity(*, entity_id: str, name: str):
        """Renames an entity (or entities) on the fly.

        Args:
            entity_id: The entity/entities to rename.
            name: The new name for the entity/entities."""
        ...

    @staticmethod
    def create_area(*, name: str, icon: str | None = None, aliases: Any | None = None):
        """Creates a new area on the fly.

        Args:
            name: The name of the area to create.
            icon: Icon to use for the area.
            aliases: A list of aliases for the area. This is useful if you want to use the area in a different language or different nickname."""
        ...

    @staticmethod
    def set_area_aliases(*, area_id, aliases: Any):
        """Sets aliases for an area. Overwrite and removed any existing aliases, fully replacing them with the new ones.

        Args:
            area_id: The ID of the area to set the aliases for.
            aliases: The aliases to set for the area."""
        ...

    @staticmethod
    def add_label_to_device(*, label_id, device_id):
        """Adds a label to a device. If multiple labels or multiple devices are provided, all combinations will be added.

        Args:
            label_id: The ID(s) of the label(s) to add the device(s).
            device_id: The ID(s) of the device(s) to add the label(s) to."""
        ...

    @staticmethod
    def add_entity_to_area(*, area_id, entity_id: str):
        """Adds an entity to an area. Please note, if the enity is already in an area, it will be removed from the previous area. This will override the area the device, that provides this entity, is in.

        Args:
            area_id: The ID of the area to add the entity to.
            entity_id: The ID of the entity (or entities) to add to the area."""
        ...


class _image_state(StateVal):
    access_token: str
    entity_picture: str

    def snapshot(self, filename: str):
        """

        Args:
            filename:  Example: /tmp/image_snapshot.jpg"""
        ...


class image:
    galaxy_tab_a7_bildschirmfoto: _image_state

    @staticmethod
    def snapshot(*, entity_id: str, filename: str):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/image_snapshot.jpg"""
        ...


class _input_boolean_state(StateVal):
    editable: bool

    def turn_on(self): ...

    def turn_off(self): ...

    def toggle(self): ...


class _input_datetime_state(StateVal):
    editable: bool
    has_date: bool
    has_time: bool
    hour: int
    minute: int
    second: int
    timestamp: int

    def set_datetime(
        self,
        *,
        date: str | None = None,
        time: str | None = None,
        datetime: str | None = None,
        timestamp: float | None = None,
    ):
        '''

        Args:
            date:  Example: "2019-04-20"
            time:  Example: "05:04:20"
            datetime:  Example: "2019-04-20 05:04:20"'''
        ...


class _input_number_state(StateVal):
    editable: bool
    initial: Any
    max: float
    min: float
    mode: str
    step: float
    unit_of_measurement: str

    def set_value(self, value: float): ...

    def max(self):
        """Set an input number entity to its maximum value."""
        ...

    def min(self):
        """Set an input number entity to its minimum value."""
        ...

    def increment(self, amount: float | None):
        """Increase an input number entity value by a certain amount.

        Args:
            amount: The amount to increase the input number with. If not provided, the step of the number entity will be used."""
        ...

    def decrement(self, amount: float | None):
        """Decrease an input number entity value by a certain amount.

        Args:
            amount: The amount to decrease the input number with. If not provided, the step of the number entity will be used."""
        ...


class input_boolean:
    coffeemaker_timer_enabled: _input_boolean_state

    @staticmethod
    def reload(): ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class input_button:
    @staticmethod
    def reload(): ...

    @staticmethod
    def press(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class input_datetime:
    attic_time_comfort_stop: _input_datetime_state
    attic_time_comfort_start: _input_datetime_state
    guestbath_time_comfort_start: _input_datetime_state
    guestbath_time_comfort_stop: _input_datetime_state
    coffeemaker_timer: _input_datetime_state
    bedroom_ben_time_comfort_start: _input_datetime_state
    bedroom_ben_time_comfort_stop: _input_datetime_state

    @staticmethod
    def reload(): ...

    @staticmethod
    def set_datetime(
        *,
        entity_id: str,
        date: str | None = None,
        time: str | None = None,
        datetime: str | None = None,
        timestamp: float | None = None,
    ):
        '''

        Args:
            entity_id: Entity ID
            date:  Example: "2019-04-20"
            time:  Example: "05:04:20"
            datetime:  Example: "2019-04-20 05:04:20"'''
        ...


class input_number:
    attic_temperature_comfort: _input_number_state
    attic_temperature_eco: _input_number_state
    guestbath_temperature_comfort: _input_number_state
    guestbath_temperature_eco: _input_number_state
    bedroom_ben_temperature_comfort: _input_number_state
    bedroom_ben_temperature_eco: _input_number_state

    @staticmethod
    def reload(): ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def max(*, entity_id: str):
        """Set an input number entity to its maximum value.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def min(*, entity_id: str):
        """Set an input number entity to its minimum value.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def increment(*, entity_id: str, amount: float | None = None):
        """Increase an input number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to increase the input number with. If not provided, the step of the number entity will be used."""
        ...

    @staticmethod
    def decrement(*, entity_id: str, amount: float | None = None):
        """Decrease an input number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to decrease the input number with. If not provided, the step of the number entity will be used."""
        ...


class input_select:
    @staticmethod
    def reload(): ...

    @staticmethod
    def select_first(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool = True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        '''

        Args:
            entity_id: Entity ID
            option:  Example: "Item A"'''
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool = True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_options(*, entity_id: str, options: str):
        """

        Args:
            entity_id: Entity ID
            options:  Example: ["Item A", "Item B", "Item C"]"""
        ...

    @staticmethod
    def random(*, entity_id: str, options: Any | None = None):
        """Select an random option for an input_select entity.

        Args:
            entity_id: Entity ID
            options: Limits the options to select from. If not provided, all options will be considered."""
        ...

    @staticmethod
    def sort(*, entity_id: str):
        """Sorts the list of selectable options for an `input_select` entity. This is not persistent and will be undone once reloaded or Home Assistant restarts.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def shuffle(*, entity_id: str):
        """Shuffles the list of selectable options for an `input_select` entity. This is not persistent and will be undone once reloaded or Home Assistant restarts.

        Args:
            entity_id: Entity ID"""
        ...


class input_text:
    @staticmethod
    def reload(): ...

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: This is an example text"""
        ...


class _light_state(StateVal):
    brightness: Any
    color_mode: str
    effect: Any
    effect_list: list
    supported_color_modes: list
    supported_features: int

    def turn_on(
        self,
        *,
        transition: int | None = None,
        rgb_color: tuple[int, int, int] | None = None,
        color_temp_kelvin: int | None = None,
        brightness_pct: int | None = None,
        brightness_step_pct: int | None = None,
        effect: str | None = None,
        rgbw_color: Any | None = None,
        rgbww_color: Any | None = None,
        color_name: Literal[
            '',
            'homeassistant',
            'aliceblue',
            'antiquewhite',
            'aqua',
            'aquamarine',
            'azure',
            'beige',
            'bisque',
            'blanchedalmond',
            'blue',
            'blueviolet',
            'brown',
            'burlywood',
            'cadetblue',
            'chartreuse',
            'chocolate',
            'coral',
            'cornflowerblue',
            'cornsilk',
            'crimson',
            'cyan',
            'darkblue',
            'darkcyan',
            'darkgoldenrod',
            'darkgray',
            'darkgreen',
            'darkgrey',
            'darkkhaki',
            'darkmagenta',
            'darkolivegreen',
            'darkorange',
            'darkorchid',
            'darkred',
            'darksalmon',
            'darkseagreen',
            'darkslateblue',
            'darkslategray',
            'darkslategrey',
            'darkturquoise',
            'darkviolet',
            'deeppink',
            'deepskyblue',
            'dimgray',
            'dimgrey',
            'dodgerblue',
            'firebrick',
            'floralwhite',
            'forestgreen',
            'fuchsia',
            'gainsboro',
            'ghostwhite',
            'gold',
            'goldenrod',
            'gray',
            'green',
            'greenyellow',
            'grey',
            'honeydew',
            'hotpink',
            'indianred',
            'indigo',
            'ivory',
            'khaki',
            'lavender',
            'lavenderblush',
            'lawngreen',
            'lemonchiffon',
            'lightblue',
            'lightcoral',
            'lightcyan',
            'lightgoldenrodyellow',
            'lightgray',
            'lightgreen',
            'lightgrey',
            'lightpink',
            'lightsalmon',
            'lightseagreen',
            'lightskyblue',
            'lightslategray',
            'lightslategrey',
            'lightsteelblue',
            'lightyellow',
            'lime',
            'limegreen',
            'linen',
            'magenta',
            'maroon',
            'mediumaquamarine',
            'mediumblue',
            'mediumorchid',
            'mediumpurple',
            'mediumseagreen',
            'mediumslateblue',
            'mediumspringgreen',
            'mediumturquoise',
            'mediumvioletred',
            'midnightblue',
            'mintcream',
            'mistyrose',
            'moccasin',
            'navajowhite',
            'navy',
            'navyblue',
            'oldlace',
            'olive',
            'olivedrab',
            'orange',
            'orangered',
            'orchid',
            'palegoldenrod',
            'palegreen',
            'paleturquoise',
            'palevioletred',
            'papayawhip',
            'peachpuff',
            'peru',
            'pink',
            'plum',
            'powderblue',
            'purple',
            'red',
            'rosybrown',
            'royalblue',
            'saddlebrown',
            'salmon',
            'sandybrown',
            'seagreen',
            'seashell',
            'sienna',
            'silver',
            'skyblue',
            'slateblue',
            'slategray',
            'slategrey',
            'snow',
            'springgreen',
            'steelblue',
            'tan',
            'teal',
            'thistle',
            'tomato',
            'turquoise',
            'violet',
            'wheat',
            'white',
            'whitesmoke',
            'yellow',
            'yellowgreen',
        ]
        | None = None,
        hs_color: Any | None = None,
        xy_color: Any | None = None,
        color_temp: int | None = None,
        brightness: int | None = None,
        brightness_step: int | None = None,
        white=None,
        profile: str | None = None,
        flash: Literal['', 'long', 'short'] | None = None,
    ):
        """

        Args:
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

    def turn_off(
        self, *, transition: int | None = None, flash: Literal['', 'long', 'short'] | None = None
    ): ...

    def toggle(
        self,
        *,
        transition: int | None = None,
        rgb_color: tuple[int, int, int] | None = None,
        color_temp_kelvin: int | None = None,
        brightness_pct: int | None = None,
        effect: str | None = None,
        rgbw_color: Any | None = None,
        rgbww_color: Any | None = None,
        color_name: Literal[
            '',
            'homeassistant',
            'aliceblue',
            'antiquewhite',
            'aqua',
            'aquamarine',
            'azure',
            'beige',
            'bisque',
            'blanchedalmond',
            'blue',
            'blueviolet',
            'brown',
            'burlywood',
            'cadetblue',
            'chartreuse',
            'chocolate',
            'coral',
            'cornflowerblue',
            'cornsilk',
            'crimson',
            'cyan',
            'darkblue',
            'darkcyan',
            'darkgoldenrod',
            'darkgray',
            'darkgreen',
            'darkgrey',
            'darkkhaki',
            'darkmagenta',
            'darkolivegreen',
            'darkorange',
            'darkorchid',
            'darkred',
            'darksalmon',
            'darkseagreen',
            'darkslateblue',
            'darkslategray',
            'darkslategrey',
            'darkturquoise',
            'darkviolet',
            'deeppink',
            'deepskyblue',
            'dimgray',
            'dimgrey',
            'dodgerblue',
            'firebrick',
            'floralwhite',
            'forestgreen',
            'fuchsia',
            'gainsboro',
            'ghostwhite',
            'gold',
            'goldenrod',
            'gray',
            'green',
            'greenyellow',
            'grey',
            'honeydew',
            'hotpink',
            'indianred',
            'indigo',
            'ivory',
            'khaki',
            'lavender',
            'lavenderblush',
            'lawngreen',
            'lemonchiffon',
            'lightblue',
            'lightcoral',
            'lightcyan',
            'lightgoldenrodyellow',
            'lightgray',
            'lightgreen',
            'lightgrey',
            'lightpink',
            'lightsalmon',
            'lightseagreen',
            'lightskyblue',
            'lightslategray',
            'lightslategrey',
            'lightsteelblue',
            'lightyellow',
            'lime',
            'limegreen',
            'linen',
            'magenta',
            'maroon',
            'mediumaquamarine',
            'mediumblue',
            'mediumorchid',
            'mediumpurple',
            'mediumseagreen',
            'mediumslateblue',
            'mediumspringgreen',
            'mediumturquoise',
            'mediumvioletred',
            'midnightblue',
            'mintcream',
            'mistyrose',
            'moccasin',
            'navajowhite',
            'navy',
            'navyblue',
            'oldlace',
            'olive',
            'olivedrab',
            'orange',
            'orangered',
            'orchid',
            'palegoldenrod',
            'palegreen',
            'paleturquoise',
            'palevioletred',
            'papayawhip',
            'peachpuff',
            'peru',
            'pink',
            'plum',
            'powderblue',
            'purple',
            'red',
            'rosybrown',
            'royalblue',
            'saddlebrown',
            'salmon',
            'sandybrown',
            'seagreen',
            'seashell',
            'sienna',
            'silver',
            'skyblue',
            'slateblue',
            'slategray',
            'slategrey',
            'snow',
            'springgreen',
            'steelblue',
            'tan',
            'teal',
            'thistle',
            'tomato',
            'turquoise',
            'violet',
            'wheat',
            'white',
            'whitesmoke',
            'yellow',
            'yellowgreen',
        ]
        | None = None,
        hs_color: Any | None = None,
        xy_color: Any | None = None,
        color_temp: int | None = None,
        brightness: int | None = None,
        white=None,
        profile: str | None = None,
        flash: Literal['', 'long', 'short'] | None = None,
    ):
        """

        Args:
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...


class light:
    office_mike_light: _light_state
    guestbath_light: _light_state
    first_floor_light: _light_state
    ground_floor_light: _light_state
    attic_balllight: _light_state
    livingroom_floorlamp_couch_right: _light_state
    livingroom_floorlamp_couch_left: _light_state
    livingroom_floorlamps_couch: _light_state
    attic_lamp_shelf: _light_state
    diningroom_light_left: _light_state
    diningroom_light_right: _light_state
    garden_light_1: _light_state
    garden_light_2: _light_state
    christmas_tree_outlet: _light_state
    bedroom_1_christmas_tree_outlet: _light_state

    @staticmethod
    def turn_on(
        *,
        entity_id: str,
        transition: int | None = None,
        rgb_color: tuple[int, int, int] | None = None,
        color_temp_kelvin: int | None = None,
        brightness_pct: int | None = None,
        brightness_step_pct: int | None = None,
        effect: str | None = None,
        rgbw_color: Any | None = None,
        rgbww_color: Any | None = None,
        color_name: Literal[
            '',
            'homeassistant',
            'aliceblue',
            'antiquewhite',
            'aqua',
            'aquamarine',
            'azure',
            'beige',
            'bisque',
            'blanchedalmond',
            'blue',
            'blueviolet',
            'brown',
            'burlywood',
            'cadetblue',
            'chartreuse',
            'chocolate',
            'coral',
            'cornflowerblue',
            'cornsilk',
            'crimson',
            'cyan',
            'darkblue',
            'darkcyan',
            'darkgoldenrod',
            'darkgray',
            'darkgreen',
            'darkgrey',
            'darkkhaki',
            'darkmagenta',
            'darkolivegreen',
            'darkorange',
            'darkorchid',
            'darkred',
            'darksalmon',
            'darkseagreen',
            'darkslateblue',
            'darkslategray',
            'darkslategrey',
            'darkturquoise',
            'darkviolet',
            'deeppink',
            'deepskyblue',
            'dimgray',
            'dimgrey',
            'dodgerblue',
            'firebrick',
            'floralwhite',
            'forestgreen',
            'fuchsia',
            'gainsboro',
            'ghostwhite',
            'gold',
            'goldenrod',
            'gray',
            'green',
            'greenyellow',
            'grey',
            'honeydew',
            'hotpink',
            'indianred',
            'indigo',
            'ivory',
            'khaki',
            'lavender',
            'lavenderblush',
            'lawngreen',
            'lemonchiffon',
            'lightblue',
            'lightcoral',
            'lightcyan',
            'lightgoldenrodyellow',
            'lightgray',
            'lightgreen',
            'lightgrey',
            'lightpink',
            'lightsalmon',
            'lightseagreen',
            'lightskyblue',
            'lightslategray',
            'lightslategrey',
            'lightsteelblue',
            'lightyellow',
            'lime',
            'limegreen',
            'linen',
            'magenta',
            'maroon',
            'mediumaquamarine',
            'mediumblue',
            'mediumorchid',
            'mediumpurple',
            'mediumseagreen',
            'mediumslateblue',
            'mediumspringgreen',
            'mediumturquoise',
            'mediumvioletred',
            'midnightblue',
            'mintcream',
            'mistyrose',
            'moccasin',
            'navajowhite',
            'navy',
            'navyblue',
            'oldlace',
            'olive',
            'olivedrab',
            'orange',
            'orangered',
            'orchid',
            'palegoldenrod',
            'palegreen',
            'paleturquoise',
            'palevioletred',
            'papayawhip',
            'peachpuff',
            'peru',
            'pink',
            'plum',
            'powderblue',
            'purple',
            'red',
            'rosybrown',
            'royalblue',
            'saddlebrown',
            'salmon',
            'sandybrown',
            'seagreen',
            'seashell',
            'sienna',
            'silver',
            'skyblue',
            'slateblue',
            'slategray',
            'slategrey',
            'snow',
            'springgreen',
            'steelblue',
            'tan',
            'teal',
            'thistle',
            'tomato',
            'turquoise',
            'violet',
            'wheat',
            'white',
            'whitesmoke',
            'yellow',
            'yellowgreen',
        ]
        | None = None,
        hs_color: Any | None = None,
        xy_color: Any | None = None,
        color_temp: int | None = None,
        brightness: int | None = None,
        brightness_step: int | None = None,
        white=None,
        profile: str | None = None,
        flash: Literal['', 'long', 'short'] | None = None,
    ):
        """

        Args:
            entity_id: Entity ID
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

    @staticmethod
    def turn_off(
        *,
        entity_id: str,
        transition: int | None = None,
        flash: Literal['', 'long', 'short'] | None = None,
    ):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(
        *,
        entity_id: str,
        transition: int | None = None,
        rgb_color: tuple[int, int, int] | None = None,
        color_temp_kelvin: int | None = None,
        brightness_pct: int | None = None,
        effect: str | None = None,
        rgbw_color: Any | None = None,
        rgbww_color: Any | None = None,
        color_name: Literal[
            '',
            'homeassistant',
            'aliceblue',
            'antiquewhite',
            'aqua',
            'aquamarine',
            'azure',
            'beige',
            'bisque',
            'blanchedalmond',
            'blue',
            'blueviolet',
            'brown',
            'burlywood',
            'cadetblue',
            'chartreuse',
            'chocolate',
            'coral',
            'cornflowerblue',
            'cornsilk',
            'crimson',
            'cyan',
            'darkblue',
            'darkcyan',
            'darkgoldenrod',
            'darkgray',
            'darkgreen',
            'darkgrey',
            'darkkhaki',
            'darkmagenta',
            'darkolivegreen',
            'darkorange',
            'darkorchid',
            'darkred',
            'darksalmon',
            'darkseagreen',
            'darkslateblue',
            'darkslategray',
            'darkslategrey',
            'darkturquoise',
            'darkviolet',
            'deeppink',
            'deepskyblue',
            'dimgray',
            'dimgrey',
            'dodgerblue',
            'firebrick',
            'floralwhite',
            'forestgreen',
            'fuchsia',
            'gainsboro',
            'ghostwhite',
            'gold',
            'goldenrod',
            'gray',
            'green',
            'greenyellow',
            'grey',
            'honeydew',
            'hotpink',
            'indianred',
            'indigo',
            'ivory',
            'khaki',
            'lavender',
            'lavenderblush',
            'lawngreen',
            'lemonchiffon',
            'lightblue',
            'lightcoral',
            'lightcyan',
            'lightgoldenrodyellow',
            'lightgray',
            'lightgreen',
            'lightgrey',
            'lightpink',
            'lightsalmon',
            'lightseagreen',
            'lightskyblue',
            'lightslategray',
            'lightslategrey',
            'lightsteelblue',
            'lightyellow',
            'lime',
            'limegreen',
            'linen',
            'magenta',
            'maroon',
            'mediumaquamarine',
            'mediumblue',
            'mediumorchid',
            'mediumpurple',
            'mediumseagreen',
            'mediumslateblue',
            'mediumspringgreen',
            'mediumturquoise',
            'mediumvioletred',
            'midnightblue',
            'mintcream',
            'mistyrose',
            'moccasin',
            'navajowhite',
            'navy',
            'navyblue',
            'oldlace',
            'olive',
            'olivedrab',
            'orange',
            'orangered',
            'orchid',
            'palegoldenrod',
            'palegreen',
            'paleturquoise',
            'palevioletred',
            'papayawhip',
            'peachpuff',
            'peru',
            'pink',
            'plum',
            'powderblue',
            'purple',
            'red',
            'rosybrown',
            'royalblue',
            'saddlebrown',
            'salmon',
            'sandybrown',
            'seagreen',
            'seashell',
            'sienna',
            'silver',
            'skyblue',
            'slateblue',
            'slategray',
            'slategrey',
            'snow',
            'springgreen',
            'steelblue',
            'tan',
            'teal',
            'thistle',
            'tomato',
            'turquoise',
            'violet',
            'wheat',
            'white',
            'whitesmoke',
            'yellow',
            'yellowgreen',
        ]
        | None = None,
        hs_color: Any | None = None,
        xy_color: Any | None = None,
        color_temp: int | None = None,
        brightness: int | None = None,
        white=None,
        profile: str | None = None,
        flash: Literal['', 'long', 'short'] | None = None,
    ):
        """

        Args:
            entity_id: Entity ID
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...


class logbook:
    @staticmethod
    def log(*, name: str, message: str, entity_id: str | None = None, domain: str | None = None):
        """

        Args:
            name:  Example: Kitchen
            message:  Example: is being used
            domain:  Example: light"""
        ...


class logger:
    @staticmethod
    def set_default_level(
        *,
        level: Literal['', 'debug', 'info', 'warning', 'error', 'fatal', 'critical'] | None = None,
    ): ...

    @staticmethod
    def set_level(): ...


class _media_player_state(StateVal):
    assumed_state: bool
    supported_features: int

    def turn_on(self): ...

    def turn_off(self): ...

    def toggle(self): ...

    def volume_up(self): ...

    def volume_down(self): ...

    def media_play_pause(self): ...

    def media_play(self): ...

    def media_pause(self): ...

    def media_stop(self): ...

    def media_next_track(self): ...

    def media_previous_track(self): ...

    def clear_playlist(self): ...

    def volume_set(self, volume_level: int): ...

    def volume_mute(self, is_volume_muted: bool): ...

    def media_seek(self, seek_position: float): ...

    def join(self, group_members: str):
        """

        Args:
            group_members:  Example: - media_player.multiroom_player2
                - media_player.multiroom_player3
        """
        ...

    def select_source(self, source: str):
        """

        Args:
            source:  Example: video1"""
        ...

    def select_sound_mode(self, sound_mode: str | None):
        """

        Args:
            sound_mode:  Example: Music"""
        ...

    def play_media(
        self,
        *,
        media,
        enqueue: Literal['', 'play', 'next', 'add', 'replace'] | None = None,
        announce: bool | None = None,
    ):
        """

        Args:
            media:  Example: {"media_content_id": "https://home-assistant.io/images/cast/splash.png", "media_content_type": "music"}
            announce:  Example: true"""
        ...

    def browse_media(
        self, *, media_content_type: str | None = None, media_content_id: str | None = None
    ) -> dict[str, Any]:
        """

        Args:
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles"""
        ...

    def search_media(
        self,
        *,
        search_query: str,
        media_content_type: str | None = None,
        media_content_id: str | None = None,
        media_filter_classes: str | None = None,
    ) -> dict[str, Any]:
        """

        Args:
            search_query:  Example: Beatles
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles
            media_filter_classes:  Example: ['album', 'artist']"""
        ...

    def shuffle_set(self, shuffle: bool): ...

    def unjoin(self): ...

    def repeat_set(self, repeat: Literal['', 'off', 'all', 'one']): ...


class media_player:
    stomp: _media_player_state
    galaxy_tab_a7: _media_player_state

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_up(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_down(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_play_pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_play(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_stop(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_next_track(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_previous_track(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clear_playlist(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_set(*, entity_id: str, volume_level: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_mute(*, entity_id: str, is_volume_muted: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_seek(*, entity_id: str, seek_position: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def join(*, entity_id: str, group_members: str):
        """

        Args:
            entity_id: Entity ID
            group_members:  Example: - media_player.multiroom_player2
                - media_player.multiroom_player3
        """
        ...

    @staticmethod
    def select_source(*, entity_id: str, source: str):
        """

        Args:
            entity_id: Entity ID
            source:  Example: video1"""
        ...

    @staticmethod
    def select_sound_mode(*, entity_id: str, sound_mode: str | None = None):
        """

        Args:
            entity_id: Entity ID
            sound_mode:  Example: Music"""
        ...

    @staticmethod
    def play_media(
        *,
        entity_id: str,
        media,
        enqueue: Literal['', 'play', 'next', 'add', 'replace'] | None = None,
        announce: bool | None = None,
    ):
        """

        Args:
            entity_id: Entity ID
            media:  Example: {"media_content_id": "https://home-assistant.io/images/cast/splash.png", "media_content_type": "music"}
            announce:  Example: true"""
        ...

    @staticmethod
    def browse_media(
        *,
        entity_id: str,
        media_content_type: str | None = None,
        media_content_id: str | None = None,
    ) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles"""
        ...

    @staticmethod
    def search_media(
        *,
        entity_id: str,
        search_query: str,
        media_content_type: str | None = None,
        media_content_id: str | None = None,
        media_filter_classes: str | None = None,
    ) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            search_query:  Example: Beatles
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles
            media_filter_classes:  Example: ['album', 'artist']"""
        ...

    @staticmethod
    def shuffle_set(*, entity_id: str, shuffle: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def unjoin(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def repeat_set(*, entity_id: str, repeat: Literal['', 'off', 'all', 'one']):
        """

        Args:
            entity_id: Entity ID"""
        ...


class mqtt:
    @staticmethod
    def publish(
        *,
        topic: str,
        payload=None,
        evaluate_payload: bool = False,
        qos: Literal['', '0', '1', '2'] = '0',
        retain: bool = False,
    ):
        """

        Args:
            topic:  Example: /homeassistant/hello
            payload:  Example: The temperature is {{ states('sensor.temperature') }}"""
        ...

    @staticmethod
    def dump(*, topic: str | None = None, duration: int = 5):
        """

        Args:
            topic:  Example: OpenZWave/#"""
        ...

    @staticmethod
    def reload(): ...


class _notify_state(StateVal):
    supported_features: int

    def send_message(self, *, message: str, title: str | None = None): ...


class notify:
    galaxy_tab_a7_overlay_nachricht: _notify_state
    galaxy_tab_a7_text_zu_sprache: _notify_state

    @staticmethod
    def send_message(*, entity_id: str, message: str, title: str | None = None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def persistent_notification(*, message: str, title: str | None = None, data: Any | None = None):
        """

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_all(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the mobile_app_all service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_iphone_von_ben(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the mobile_app_iphone_von_ben integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_ben_pagel(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the mobile_app_ben_pagel integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_public_tablet(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the mobile_app_public_tablet integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_sm_g780g(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the mobile_app_sm_g780g integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def mobile_app_s22_mike(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the mobile_app_s22_mike integration.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

    @staticmethod
    def notify(
        *,
        message: str,
        title: str | None = None,
        target: Any | None = None,
        data: Any | None = None,
    ):
        """Sends a notification message using the notify service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...


class _number_state(StateVal):
    max: float | int
    min: float | int
    mode: str
    step: float | int
    unit_of_measurement: str

    def set_value(self, value: str):
        """

        Args:
            value:  Example: 42"""
        ...

    def max(self):
        """Set a number entity to its maximum value."""
        ...

    def min(self):
        """Set a number entity to its minimum value."""
        ...

    def increment(self, amount: float | None):
        """Increase a number entity value by a certain amount.

        Args:
            amount: The amount to increase the number with. If not provided, the step of the number entity will be used."""
        ...

    def decrement(self, amount: float | None):
        """Decrease a number entity value by a certain amount.

        Args:
            amount: The amount to decrease the number with. If not provided, the step of the number entity will be used."""
        ...


class number:
    galaxy_tab_a7_bildschirmschoner_timer: _number_state
    galaxy_tab_a7_bildschirmschoner_helligkeit: _number_state
    galaxy_tab_a7_bildschirm_aus_timer: _number_state
    galaxy_tab_a7_bildschirmhelligkeit: _number_state
    guestbath_radiator_open_window_temperature: _number_state
    guestbath_radiator_comfort_temperature: _number_state
    guestbath_radiator_eco_temperature: _number_state
    guestbath_radiator_local_temperature_calibration: _number_state
    guestbath_radiator_boost_timeset_countdown: _number_state
    guestbath_radiator_holiday_temperature: _number_state
    bedroom_ben_radiator_external_temperature_input: _number_state
    bedroom_ben_radiator_away_preset_temperature: _number_state

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: 42"""
        ...

    @staticmethod
    def max(*, entity_id: str):
        """Set a number entity to its maximum value.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def min(*, entity_id: str):
        """Set a number entity to its minimum value.

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def increment(*, entity_id: str, amount: float | None = None):
        """Increase a number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to increase the number with. If not provided, the step of the number entity will be used."""
        ...

    @staticmethod
    def decrement(*, entity_id: str, amount: float | None = None):
        """Decrease a number entity value by a certain amount.

        Args:
            entity_id: Entity ID
            amount: The amount to decrease the number with. If not provided, the step of the number entity will be used."""
        ...


class persistent_notification:
    @staticmethod
    def create(*, message: str, title: str | None = None, notification_id: str | None = None):
        """

        Args:
            message:  Example: Please check your configuration.yaml.
            title:  Example: Test notification
            notification_id:  Example: 1234"""
        ...

    @staticmethod
    def dismiss(*, notification_id: str):
        """

        Args:
            notification_id:  Example: 1234"""
        ...

    @staticmethod
    def dismiss_all(): ...


class _person_state(StateVal):
    device_trackers: list
    editable: bool
    entity_picture: str
    gps_accuracy: int
    id: str
    latitude: float
    longitude: float
    source: str
    user_id: str


class person:
    mike_pagel: _person_state
    britta_pagel: _person_state
    ben_pagel: _person_state

    @staticmethod
    def reload(): ...

    @staticmethod
    def remove_device_tracker(*, entity_id: str, device_tracker: str):
        """Remove a device tracker from a person.

        Args:
            entity_id: The person entity ID to remove the device tracker from.
            device_tracker: The device tracker entity ID to remove from the person."""
        ...

    @staticmethod
    def add_device_tracker(*, entity_id: str, device_tracker: str):
        """Add a device tracker to a person.

        Args:
            entity_id: The person entity ID to add the device tracker to.
            device_tracker: The device tracker entity ID to add to the person."""
        ...


class presence_simulation:
    @staticmethod
    def start(
        *,
        switch_id=None,
        entity_id=None,
        delta=None,
        restore_states=None,
        random=None,
        brightness=None,
    ):
        """Start the presence simulation

        Args:
            switch_id: The id of the presence simulation switch Example: switch.presence_simulation_2
            entity_id: The list of entities to use by the presence simulation to override the list configured in the component Example: - group.outside_lights

            delta: Override the default number of days used by the simulation Example: 7
            restore_states: Override the default restore switch. If set, the states will be restored after the simulation Example: True
            random: Add a random factor (in seconds) to the historic events Example: 300
            brightness: Set a specific brightness fot lights that allows it Example: 75"""
        ...

    @staticmethod
    def stop(*, switch_id=None):
        """Stop the presence simulation

        Args:
            switch_id: The id of the presence simulation switch Example: switch.presence_simulation_2"""
        ...

    @staticmethod
    def toggle(*, switch_id=None):
        """Toggle the presence simulation

        Args:
            switch_id: The id of the presence simulation switch Example: switch.presence_simulation_2"""
        ...


class pyscript:
    @staticmethod
    def hello_world(*, action=None, id=None):
        """hello_world example using pyscript.

        Args:
            action: argument action
            id: argument id"""
        ...

    @staticmethod
    def reload(*, global_ctx: str | None = None):
        """Reloads all available pyscripts and restart triggers

        Args:
            global_ctx: Only reload this specific global context (file or app) Example: file.example"""
        ...

    @staticmethod
    def generate_stubs() -> dict[str, Any]:
        """Build a stub files combining builtin helpers with discovered entities and services."""
        ...

    @staticmethod
    def jupyter_kernel_start(
        *,
        key: str,
        kernel_name: str = 'pyscript',
        shell_port: int | None = None,
        iopub_port: int | None = None,
        stdin_port: int | None = None,
        control_port: int | None = None,
        hb_port: int | None = None,
        ip: str = '127.0.0.1',
        transport: Literal['', 'tcp', 'udp'] = 'tcp',
        signature_scheme: Literal['', 'hmac-sha256'] = 'hmac-sha256',
    ):
        """Starts a jupyter kernel for interactive use; Called by Jupyter front end and should generally not be used by users

        Args:
            key: Used for signing Example: 012345678-9abcdef023456789abcdef
            kernel_name: Kernel name Example: pyscript
            shell_port: Shell port number Example: 63599
            iopub_port: IOPub port number Example: 63598
            stdin_port: Stdin port number Example: 63597
            control_port: Control port number Example: 63596
            hb_port: Heartbeat port number Example: 63595
            ip: IP address to connect to Jupyter front end Example: 127.0.0.1
            transport: Transport type Example: tcp
            signature_scheme: Signing algorithm Example: hmac-sha256"""
        ...


class recorder:
    @staticmethod
    def purge(
        *, keep_days: int | None = None, repack: bool = False, apply_filter: bool = False
    ): ...

    @staticmethod
    def purge_entities(
        *,
        entity_id: str | None = None,
        domains: Any | None = None,
        entity_globs: Any | None = None,
        keep_days: int = 0,
    ):
        """

        Args:
            domains:  Example: sun
            entity_globs:  Example: domain*.object_id*"""
        ...

    @staticmethod
    def enable(): ...

    @staticmethod
    def disable(): ...

    @staticmethod
    def get_statistics(
        *,
        start_time: datetime,
        statistic_ids,
        period: Literal['', '5minute', 'hour', 'day', 'week', 'month'],
        types: Literal['', 'change', 'last_reset', 'max', 'mean', 'min', 'state', 'sum'],
        end_time: datetime | None = None,
        units: Any | None = None,
    ) -> dict[str, Any]:
        """

        Args:
            start_time:  Example: 2025-01-01 00:00:00
            statistic_ids:  Example: ['sensor.energy_consumption', 'sensor.temperature']
            period:  Example: hour
            types:  Example: ['mean', 'sum']
            end_time:  Example: 2025-01-02 00:00:00
            units:  Example: {'energy': 'kWh', 'temperature': '°C'}"""
        ...

    @staticmethod
    def import_statistics(
        *,
        statistic_id: str,
        source: str,
        has_mean: bool,
        has_sum: bool,
        stats: Any,
        name: str | None = None,
        unit_of_measurement: str | None = None,
    ):
        """Import long-term statistics.

        Args:
            statistic_id: The statistics ID (entity ID) to import for.
            source: The source of the statistics data.
            has_mean: If the statistics has a mean value.
            has_sum: If the statistics has a sum value.
            stats: A list of mappings/dictionaries with statistics to import. The dictionaries must contain a "start" key with a datetime string other valid options are "mean", "sum", "min", "max", "last_reset", and "state". All of those are optional and either an integer or a float, except for "last_reset" which is a datetime string.
            name: The name of the statistics.
            unit_of_measurement: The unit of measurement of the statistics."""
        ...


class repairs:
    @staticmethod
    def remove(*, issue_id: str):
        """Removes a manually created Home Assistant repairs issue. This action can only remove issues created with the `repairs_create` action.

        Args:
            issue_id: The issue ID to remove."""
        ...

    @staticmethod
    def create(
        *,
        title: str,
        description: str,
        issue_id: str | None = None,
        domain: str | None = None,
        severity: Literal['', 'warning', 'error', 'critical'] | None = None,
        persistent: bool | None = None,
    ):
        """Manually create and raise a issue in Home Assistant repairs.

        Args:
            title: The title of the issue.
            description: The description of the issue. Supports Markdown.
            issue_id: The issue can have an identifier, which allows you to cancel it later with that ID if needed. It also prevent duplicate issues to be created. If not provided, a random ID will be generated.
            domain: This field can be used to set the domain of the issue. For example, by default (if not set), it will use "spook". This causes Spook to be shown in the logo/image of the issue. If you set it to "homeassistant", the Home Assistant logo will be used, or use "hue", "zwave_js", "mqtt", etc. to use the logo of that integration.
            severity: The severity of the issue. This will be used to determine the priority of the issue. If not set, "warning" will be used
            persistent: If the issue should be persistent, which means it will survive restarts of Home Assistant. By default, issues are not persistent."""
        ...

    @staticmethod
    def unignore_all():
        """Unignore all issues currently raised in Home Assistant Repairs."""
        ...

    @staticmethod
    def ignore_all():
        """Ignore all issues currently raised in Home Assistant Repairs."""
        ...


class rest_command:
    @staticmethod
    def update_cloudflare_mpagel_de_aaaa() -> dict[str, Any]: ...

    @staticmethod
    def reload(): ...


class scene:
    @staticmethod
    def reload(): ...

    @staticmethod
    def apply(*, entities: Any, transition: int | None = None):
        """

        Args:
            entities:  Example: light.kitchen: "on"
                light.ceiling:
                  state: "on"
                  brightness: 80
        """
        ...

    @staticmethod
    def create(*, scene_id: str, entities: Any | None = None, snapshot_entities: str | None = None):
        """

        Args:
            scene_id:  Example: all_lights
            entities:  Example: light.tv_back_light: "on"
                light.ceiling:
                  state: "on"
                  brightness: 200

            snapshot_entities:  Example: - light.ceiling
                - light.kitchen
        """
        ...

    @staticmethod
    def delete(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str, transition: int | None = None):
        """

        Args:
            entity_id: Entity ID"""
        ...


class schedule:
    @staticmethod
    def reload(): ...

    @staticmethod
    def get_schedule(*, entity_id: str) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...


class _script_state(StateVal):
    current: int
    last_triggered: datetime
    mode: str
    restored: bool
    supported_features: int

    def turn_on(self): ...

    def turn_off(self): ...

    def toggle(self): ...


class script:
    fire_ad_event: _script_state
    fire_ad_trigger: _script_state

    @staticmethod
    def fire_ad_trigger() -> dict[str, Any]: ...

    @staticmethod
    def reload(): ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class _select_state(StateVal):
    options: list

    def select_first(self): ...

    def select_last(self): ...

    def select_next(self, cycle: bool): ...

    def select_option(self, option: str):
        '''

        Args:
            option:  Example: "Item A"'''
        ...

    def select_previous(self, cycle: bool): ...

    def random(self, options: Any | None):
        """Select an random option for a select entity.

        Args:
            options: Limits the options to select from. If not provided, all options will be considered."""
        ...


class select:
    zigbee2mqtt_bridge_log_level: _select_state
    attic_lamp_shelf_power_outage_memory: _select_state
    attic_lamp_shelf_indicator_mode: _select_state
    attic_balllight_power_on_behavior: _select_state
    diningroom_light_left_power_outage_memory: _select_state
    diningroom_light_left_indicator_mode: _select_state
    diningroom_light_right_power_outage_memory: _select_state
    diningroom_light_right_indicator_mode: _select_state
    livingroom_floorlamp_couch_right_power_on_behavior: _select_state
    livingroom_floorlamp_couch_left_power_on_behavior: _select_state
    dressingroom_switch_lights_attic_click_mode: _select_state
    dressingroom_switch_lights_attic_operation_mode: _select_state
    diningroom_switch_lights_click_mode: _select_state
    diningroom_switch_lights_operation_mode: _select_state
    livingroom_switch_floorlamps_couch_click_mode: _select_state
    m5stack_atom_echo_1_0dbb0c_assist_pipeline: _select_state
    m5stack_atom_echo_1_0dbb0c_zu_ende_gesprochen_erkennung: _select_state
    guestbath_radiator_working_day: _select_state
    bedroom_ben_radiator_sensor: _select_state
    garden_light_1_power_on_behavior: _select_state
    garden_light_2_power_on_behavior: _select_state
    christmas_tree_outlet_power_outage_memory: _select_state
    christmas_tree_outlet_indicator_mode: _select_state
    m5stack_atom_echo_1_0dbb0c_aktivierungswort: _select_state
    m5stack_atom_echo_1_0dbb0c_assistent_2: _select_state
    m5stack_atom_echo_1_0dbb0c_aktivierungswort_2: _select_state
    bedroom_1_christmas_tree_outlet_power_outage_memory: _select_state
    bedroom_1_christmas_tree_outlet_indicator_mode: _select_state

    @staticmethod
    def select_first(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool = True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        '''

        Args:
            entity_id: Entity ID
            option:  Example: "Item A"'''
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool = True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def random(*, entity_id: str, options: Any | None = None):
        """Select an random option for a select entity.

        Args:
            entity_id: Entity ID
            options: Limits the options to select from. If not provided, all options will be considered."""
        ...


class _sensor_state(StateVal):
    Available: str
    Confidence: str
    Country: str
    Locality: str
    Location: list
    Name: str
    Ocean: str
    Thoroughfare: str
    Total: str
    Types: list
    Zones: list
    administrative_area: str
    command_set: Any
    country: str
    full_url: str
    info: str
    iso_country_code: str
    locality: str
    location: str | list
    marker_high_level: int
    marker_low_level: int
    marker_type: str
    name: str
    options: list
    phone: str
    postal_code: str
    premises: str
    restored: bool
    serial: Any
    state_class: str
    state_message: str
    state_reason: Any
    sub_administrative_area: str
    sub_locality: str
    sub_thoroughfare: str
    supported_features: int
    thoroughfare: str
    truncated: bool
    unit_of_measurement: str
    uri_supported: str
    url: str


class sensor:
    printer_printlex: _sensor_state
    disk_use_percent: _sensor_state
    memory_use_percent: _sensor_state
    swap_use_percent: _sensor_state
    load_5m: _sensor_state
    processor_use: _sensor_state
    processor_temperature: _sensor_state
    laundry_washer_energy: _sensor_state
    laundry_washer_power: _sensor_state
    laundry_dryer_energy: _sensor_state
    laundry_dryer_power: _sensor_state
    sun_next_dawn: _sensor_state
    sun_next_dusk: _sensor_state
    sun_next_midnight: _sensor_state
    sun_next_noon: _sensor_state
    sun_next_rising: _sensor_state
    sun_next_setting: _sensor_state
    lexmark_b2546dw_black: _sensor_state
    attic_radiator_aktuelle_geplante_voreinstellung: _sensor_state
    attic_radiator_batterie: _sensor_state
    attic_radiator_eco_temperatur: _sensor_state
    attic_radiator_komfort_temperatur: _sensor_state
    attic_radiator_nachste_geplante_anderungszeit: _sensor_state
    attic_radiator_nachste_geplante_temperatur: _sensor_state
    attic_radiator_nachste_geplante_voreinstellung: _sensor_state
    local_ip: _sensor_state
    ipv6_address_wlan0: _sensor_state
    iphone_von_ben_activity: _sensor_state
    iphone_von_ben_distance: _sensor_state
    iphone_von_ben_floors_ascended: _sensor_state
    iphone_von_ben_floors_descended: _sensor_state
    iphone_von_ben_steps: _sensor_state
    iphone_von_ben_average_active_pace: _sensor_state
    iphone_von_ben_battery_level: _sensor_state
    iphone_von_ben_battery_state: _sensor_state
    iphone_von_ben_storage: _sensor_state
    iphone_von_ben_ssid: _sensor_state
    iphone_von_ben_bssid: _sensor_state
    iphone_von_ben_connection_type: _sensor_state
    iphone_von_ben_sim_1: _sensor_state
    iphone_von_ben_sim_2: _sensor_state
    iphone_von_ben_last_update_trigger: _sensor_state
    ben_pagel_activity: _sensor_state
    ben_pagel_distance: _sensor_state
    ben_pagel_floors_ascended: _sensor_state
    ben_pagel_floors_descended: _sensor_state
    ben_pagel_steps: _sensor_state
    ben_pagel_average_active_pace: _sensor_state
    ben_pagel_battery_level: _sensor_state
    ben_pagel_battery_state: _sensor_state
    ben_pagel_storage: _sensor_state
    ben_pagel_ssid: _sensor_state
    ben_pagel_bssid: _sensor_state
    ben_pagel_connection_type: _sensor_state
    ben_pagel_sim_2: _sensor_state
    ben_pagel_sim_1: _sensor_state
    ben_pagel_geocoded_location: _sensor_state
    ben_pagel_last_update_trigger: _sensor_state
    first_floor_light_power: _sensor_state
    ground_floor_light_power: _sensor_state
    first_floor_light_energy: _sensor_state
    ground_floor_light_energy: _sensor_state
    diamex_ir_power_last_restart_time: _sensor_state
    diamex_ir_power_wifi_connect_count: _sensor_state
    diamex_ir_power_mqtt_connect_count: _sensor_state
    diamex_ir_power_restart_reason: _sensor_state
    diamex_ir_power_ssid: _sensor_state
    diamex_ir_power_sm_1_8_1: _sensor_state
    diamex_ir_power_sm_1_8_2: _sensor_state
    diamex_ir_power_sm_2_8_0: _sensor_state
    diamex_ir_power_sm_16_7_0: _sensor_state
    diamex_ir_power_sm_36_7_0: _sensor_state
    diamex_ir_power_sm_56_7_0: _sensor_state
    diamex_ir_power_sm_76_7_0: _sensor_state
    diamex_ir_power_sm_32_7_0: _sensor_state
    diamex_ir_power_sm_52_7_0: _sensor_state
    diamex_ir_power_sm_72_7_0: _sensor_state
    diamex_ir_power_sm_1_8_0: _sensor_state
    diamex_ir_power_sm_96_1_0: _sensor_state
    verbrauchte_leistung_gesamt: _sensor_state
    verbrauchte_leistung_gesamt_2: _sensor_state
    shelly_flood_12_temperature: _sensor_state
    shelly_flood_12_battery: _sensor_state
    shelly_flood_11_temperature: _sensor_state
    shelly_flood_11_battery: _sensor_state
    shelly_flood_10_temperature: _sensor_state
    shelly_flood_10_battery: _sensor_state
    coffeemaker_energy: _sensor_state
    coffeemaker_power: _sensor_state
    zigbee2mqtt_bridge_version: _sensor_state
    attic_lamp_shelf_power: _sensor_state
    attic_lamp_shelf_energy: _sensor_state
    diningroom_light_left_power: _sensor_state
    diningroom_light_left_energy: _sensor_state
    diningroom_light_right_power: _sensor_state
    diningroom_light_right_energy: _sensor_state
    dressingroom_switch_lights_attic_battery: _sensor_state
    diningroom_switch_lights_battery: _sensor_state
    livingroom_switch_floorlamps_couch_battery: _sensor_state
    attic_switch_lights_battery: _sensor_state
    attic_window_2_battery: _sensor_state
    attic_window_2_device_temperature: _sensor_state
    air_quality: _sensor_state
    alarm_control_panels: _sensor_state
    areas: _sensor_state
    automations: _sensor_state
    binary_sensors: _sensor_state
    buttons: _sensor_state
    calendars: _sensor_state
    cameras: _sensor_state
    climate: _sensor_state
    covers: _sensor_state
    dates: _sensor_state
    datetimes: _sensor_state
    devices: _sensor_state
    device_trackers: _sensor_state
    entities: _sensor_state
    fans: _sensor_state
    humidifiers: _sensor_state
    integrations: _sensor_state
    custom_integrations: _sensor_state
    input_booleans: _sensor_state
    input_buttons: _sensor_state
    input_datetimes: _sensor_state
    input_numbers: _sensor_state
    input_selects: _sensor_state
    input_texts: _sensor_state
    images: _sensor_state
    lights: _sensor_state
    locks: _sensor_state
    media_players: _sensor_state
    numbers: _sensor_state
    persistent_notifications: _sensor_state
    persons: _sensor_state
    remotes: _sensor_state
    scenes: _sensor_state
    scripts: _sensor_state
    selects: _sensor_state
    sensors: _sensor_state
    sirens: _sensor_state
    suns: _sensor_state
    stt: _sensor_state
    switches: _sensor_state
    texts: _sensor_state
    times: _sensor_state
    tts: _sensor_state
    vacuums: _sensor_state
    update: _sensor_state
    water_heaters: _sensor_state
    weather: _sensor_state
    zones: _sensor_state
    issues: _sensor_state
    active_issues: _sensor_state
    ignored_issues: _sensor_state
    public_tablet_battery_level: _sensor_state
    public_tablet_battery_state: _sensor_state
    public_tablet_charger_type: _sensor_state
    galaxy_tab_a7_batterie: _sensor_state
    galaxy_tab_a7_aktuelle_seite: _sensor_state
    galaxy_tab_a7_bildschirmausrichtung: _sensor_state
    galaxy_tab_a7_interner_freier_speicherplatz: _sensor_state
    galaxy_tab_a7_interner_speicherplatz_insgesamt: _sensor_state
    galaxy_tab_a7_freier_speicher: _sensor_state
    galaxy_tab_a7_gesamtspeicher: _sensor_state
    clock_date: _sensor_state
    clock_time: _sensor_state
    galaxy_tab_a7_vordergrund_app: _sensor_state
    ben_pagel_app_version: _sensor_state
    ben_pagel_location_permission: _sensor_state
    ben_pagel_watch_battery: _sensor_state
    ben_pagel_watch_battery_state: _sensor_state
    guestbath_radiator_schedule_monday: _sensor_state
    guestbath_radiator_schedule_tuesday: _sensor_state
    guestbath_radiator_schedule_wednesday: _sensor_state
    guestbath_radiator_schedule_thursday: _sensor_state
    guestbath_radiator_schedule_friday: _sensor_state
    guestbath_radiator_schedule_saturday: _sensor_state
    guestbath_radiator_schedule_sunday: _sensor_state
    guestbath_radiator_error_status: _sensor_state
    bedroom_ben_radiator_battery: _sensor_state
    bedroom_ben_radiator_device_temperature: _sensor_state
    bedroom_ben_window_battery: _sensor_state
    bedroom_ben_window_device_temperature: _sensor_state
    bedroom_ben_climate_battery: _sensor_state
    bedroom_ben_climate_temperature: _sensor_state
    bedroom_ben_climate_humidity: _sensor_state
    bedroom_ben_climate_pressure: _sensor_state
    sm_g780g_battery_level: _sensor_state
    sm_g780g_battery_state: _sensor_state
    sm_g780g_charger_type: _sensor_state
    sm_g780g_geocoded_location: _sensor_state
    s22_mike_battery_level: _sensor_state
    s22_mike_battery_state: _sensor_state
    s22_mike_charger_type: _sensor_state
    christmas_tree_outlet_power: _sensor_state
    christmas_tree_outlet_energy: _sensor_state
    guestbath_window_battery: _sensor_state
    guestbath_window_device_temperature: _sensor_state
    ben_pagel_audio_output: _sensor_state
    attic_climate_temperature: _sensor_state
    attic_climate_humidity: _sensor_state
    attic_climate_pressure: _sensor_state
    attic_climate_device_temperature: _sensor_state
    attic_climate_battery: _sensor_state
    backup_backup_manager_zustand: _sensor_state
    backup_nachstes_geplantes_automatisches_backup: _sensor_state
    backup_letztes_erfolgreiches_automatisches_backup: _sensor_state
    backup_zuletzt_versuchtes_automatisches_backup: _sensor_state
    attic_window_battery: _sensor_state
    guestbath_climate_battery: _sensor_state
    guestbath_climate_temperature: _sensor_state
    guestbath_climate_humidity: _sensor_state
    guestbath_climate_pressure: _sensor_state
    attic_radiator_temperatur: _sensor_state
    bedroom_1_christmas_tree_outlet_power: _sensor_state
    bedroom_1_christmas_tree_outlet_current: _sensor_state
    bedroom_1_christmas_tree_outlet_voltage: _sensor_state
    bedroom_1_christmas_tree_outlet_energy: _sensor_state
    bedroom_1_christmas_tree_outlet_linkquality: _sensor_state
    bedroom_1_christmas_tree_outlet_last_seen: _sensor_state


class spook:
    @staticmethod
    def random_fail():
        """Performing this action will randomly fail."""
        ...

    @staticmethod
    def boo():
        """Calling this action spooks Home Assistant. Performing this action will always fail."""
        ...


class _stt_state(StateVal): ...


class stt:
    home_assistant_cloud: _stt_state


class _switch_state(StateVal):
    restored: bool
    supported_features: int

    def turn_off(self): ...

    def turn_on(self): ...

    def toggle(self): ...


class switch:
    laundry_washer: _switch_state
    laundry_dryer: _switch_state
    presence_simulation: _switch_state
    zigbee2mqtt_bridge_permit_join: _switch_state
    attic_lamp_shelf: _switch_state
    diningroom_light_left: _switch_state
    diningroom_light_right: _switch_state
    cloud_alexa: _switch_state
    cloud_alexa_report_state: _switch_state
    cloud_google: _switch_state
    cloud_google_report_state: _switch_state
    cloud_remote: _switch_state
    outlet_coffeemaker: _switch_state
    galaxy_tab_a7_bildschirmschoner: _switch_state
    galaxy_tab_a7_wartungsmodus: _switch_state
    galaxy_tab_a7_kiosk_schloss: _switch_state
    galaxy_tab_a7_bewegungserkennung: _switch_state
    galaxy_tab_a7_bildschirm: _switch_state
    m5stack_atom_echo_0dbb0c_use_wake_word: _switch_state
    m5stack_atom_echo_0dbb0c_use_listen_light: _switch_state
    guestbath_radiator_open_window: _switch_state
    guestbath_radiator_heating_stop: _switch_state
    guestbath_radiator_frost_protection: _switch_state
    guestbath_radiator_online: _switch_state
    bedroom_ben_radiator_child_lock: _switch_state
    bedroom_ben_radiator_window_detection: _switch_state
    bedroom_ben_radiator_valve_detection: _switch_state
    bedroom_ben_radiator_schedule: _switch_state
    garden_light_1: _switch_state
    garden_light_2: _switch_state
    christmas_tree_outlet: _switch_state
    christmas_tree_outlet_child_lock: _switch_state
    attic_lamp_shelf_child_lock: _switch_state
    diningroom_light_left_child_lock: _switch_state
    diningroom_light_right_child_lock: _switch_state
    guestbath_radiator_child_lock: _switch_state
    bedroom_1_christmas_tree_outlet: _switch_state
    bedroom_1_christmas_tree_outlet_child_lock: _switch_state

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class system_log:
    @staticmethod
    def clear(): ...

    @staticmethod
    def write(
        *,
        message: str,
        level: Literal['', 'debug', 'info', 'warning', 'error', 'critical'] = 'error',
        logger: str | None = None,
    ):
        """

        Args:
            message:  Example: Something went wrong
            logger:  Example: mycomponent.myplatform"""
        ...


class template:
    @staticmethod
    def reload(): ...


class _text_state(StateVal):
    max: int
    min: int
    mode: str
    pattern: Any

    def set_value(self, value: str):
        """

        Args:
            value:  Example: Hello world!"""
        ...


class text:
    guestbath_radiator_holiday_start_stop: _text_state
    bedroom_ben_radiator_schedule_settings: _text_state

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: Hello world!"""
        ...


class time:
    @staticmethod
    def set_value(*, entity_id: str, time: str):
        """

        Args:
            entity_id: Entity ID
            time:  Example: 22:15"""
        ...


class timer:
    @staticmethod
    def reload(): ...

    @staticmethod
    def start(*, entity_id: str, duration: str | None = None):
        """

        Args:
            entity_id: Entity ID
            duration:  Example: 00:01:00 or 60"""
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def cancel(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def finish(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def change(*, entity_id: str, duration: str = '0'):
        """

        Args:
            entity_id: Entity ID
            duration:  Example: 00:01:00, 60 or -60"""
        ...

    @staticmethod
    def set_duration(*, entity_id: str, duration: str):
        """Set duration for an existing timer.

        Args:
            entity_id: Entity ID
            duration: New duration for the timer, as a timedelta string. Example: 00:01:00, 60"""
        ...


class _tts_state(StateVal):
    def speak(
        self,
        *,
        media_player_entity_id: str,
        message: str,
        cache: bool = True,
        language: str | None = None,
        options: Any | None = None,
    ):
        """

        Args:
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...


class tts:
    home_assistant_cloud: _tts_state

    @staticmethod
    def speak(
        *,
        entity_id: str,
        media_player_entity_id: str,
        message: str,
        cache: bool = True,
        language: str | None = None,
        options: Any | None = None,
    ):
        """

        Args:
            entity_id: Entity ID
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

    @staticmethod
    def clear_cache(): ...

    @staticmethod
    def cloud_say(
        *,
        entity_id: str,
        message: str,
        cache: bool = False,
        language: str | None = None,
        options: Any | None = None,
    ):
        """Say something using text-to-speech on a media player with cloud.

        Args:
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...


class _update_state(StateVal):
    auto_update: bool
    display_precision: int
    entity_picture: str
    in_progress: bool
    installed_version: str
    latest_version: str
    release_summary: Any
    release_url: str
    restored: bool
    skipped_version: Any
    supported_features: int
    title: str
    update_percentage: Any

    def install(self, *, version: str | None = None, backup: bool | None = None):
        """

        Args:
            version:  Example: 1.0.0"""
        ...

    def skip(self): ...

    def clear_skipped(self): ...


class update:
    home_assistant_supervisor_update: _update_state
    home_assistant_core_update: _update_state
    home_assistant_operating_system_update: _update_state
    studio_code_server_update: _update_state
    mosquitto_broker_update: _update_state
    ssh_web_terminal_update: _update_state
    appdaemon_update: _update_state
    zigbee2mqtt_update: _update_state
    laundry_washer_firmware_update: _update_state
    laundry_dryer_firmware_update: _update_state
    rtsptoweb_webrtc_update: _update_state
    mariadb_update: _update_state
    nginx_proxy_manager_update: _update_state
    shelly_pro2pm_06_firmware_update: _update_state
    logspout_addon_update: _update_state
    coffeemaker_firmware_update: _update_state
    attic_lamp_shelf: _update_state
    attic_balllight: _update_state
    diningroom_light_left: _update_state
    diningroom_light_right: _update_state
    livingroom_floorlamp_couch_right: _update_state
    livingroom_floorlamp_couch_left: _update_state
    openwakeword_update: _update_state
    esphome_update: _update_state
    battery_state_card_entity_row_update: _update_state
    auto_entities_update: _update_state
    layout_card_update: _update_state
    tapo_cameras_control_update: _update_state
    kiosk_mode_update: _update_state
    spook_your_homie_update: _update_state
    presence_simulation_update: _update_state
    multiple_entity_row_update: _update_state
    hacs_update: _update_state
    mushroom_update: _update_state
    guestbath_radiator: _update_state
    bedroom_ben_radiator: _update_state
    christmas_tree_outlet: _update_state
    attic_climate: _update_state
    bedroom_1_christmas_tree_outlet: _update_state

    @staticmethod
    def install(*, entity_id: str, version: str | None = None, backup: bool | None = None):
        """

        Args:
            entity_id: Entity ID
            version:  Example: 1.0.0"""
        ...

    @staticmethod
    def skip(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clear_skipped(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class valve:
    @staticmethod
    def open_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_valve_position(*, entity_id: str, position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...


class _wake_word_state(StateVal): ...


class wake_word:
    openwakeword: _wake_word_state


class _weather_state(StateVal):
    attribution: str
    cloud_coverage: float
    dew_point: float
    humidity: int
    precipitation_unit: str
    pressure: float
    pressure_unit: str
    supported_features: int
    temperature: float
    temperature_unit: str
    uv_index: float
    visibility_unit: str
    wind_bearing: float
    wind_speed: float
    wind_speed_unit: str

    def get_forecasts(
        self, type: Literal['', 'daily', 'hourly', 'twice_daily']
    ) -> dict[str, Any]: ...


class weather:
    forecast_home: _weather_state

    @staticmethod
    def get_forecasts(
        *, entity_id: str, type: Literal['', 'daily', 'hourly', 'twice_daily']
    ) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...


class _zone_state(StateVal):
    editable: bool
    latitude: float
    longitude: float
    passive: bool
    persons: list
    radius: float


class zone:
    antonia: _zone_state
    edk_etterschlag: _zone_state
    moni_2: _zone_state
    tristan: _zone_state
    wkr: _zone_state
    seniorenheim_jesenwang: _zone_state
    fischer_stegen: _zone_state
    hardys_hasenheide: _zone_state
    wohnung_ben: _zone_state

    @staticmethod
    def reload(): ...

    @staticmethod
    def create(
        *,
        name: str,
        latitude: float,
        longitude: float,
        icon: str | None = None,
        radius: float = 100,
    ):
        """Create a new zone in Home Assistant on the fly.

        Args:
            name: Name of the zone
            latitude: Latitude of the zone
            longitude: Longitude of the zone
            icon: Icon to use for the zone
            radius: Radius of the zone"""
        ...

    @staticmethod
    def delete(*, entity_id: str):
        """Delete a zone. This works only with zones created and managed via the UI. Zones created and managed in YAML cannot be managed by Spook.

        Args:
            entity_id: The ID of the entity (or entities) to remove."""
        ...

    @staticmethod
    def update(
        *,
        entity_id: str,
        name: str | None = None,
        icon: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        radius: float = 100,
    ):
        """Update properties of a zone on the fly.

        Args:
            entity_id: The ID of the entity (or entities) to update.
            name: Name of the zone
            icon: Icon to use for the zone
            latitude: Latitude of the zone
            longitude: Longitude of the zone
            radius: Radius of the zone"""
        ...
