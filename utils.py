# -*- coding: utf-8 -*-
"""
温室气体排放核算方法
按行业分类整理的排放计算公式
"""

#################################################
# 1. 电力行业排放计算
#################################################


class PowerIndustryEmissions:
    @staticmethod
    def calculate_sf6_emission(
        retired_equipment_sf6_capacity,
        repaired_equipment_sf6_capacity,
        retired_equipment_sf6_recovery,
        repaired_equipment_sf6_recovery,
        retired_equipment_num,
        repaired_equipment_num,
    ):
        """使用六氟化硫设备修理与退役过程产生的排放计算"""
        sf6_emission = (
            (retired_equipment_sf6_capacity - retired_equipment_sf6_recovery) * 23900
            + (repaired_equipment_sf6_capacity - repaired_equipment_sf6_recovery)
            * 23900
        ) * retired_equipment_num + (
            (repaired_equipment_sf6_capacity - repaired_equipment_sf6_recovery) * 23900
        ) * repaired_equipment_num
        return sf6_emission

    @staticmethod
    def calculate_transmission_loss_emission(
        supply_electricity, sold_electricity, regional_grid_emission_factor
    ):
        """输配电损失引起的二氧化碳排放计算"""
        transmission_loss_electricity = supply_electricity - sold_electricity
        transmission_loss_emission = (
            transmission_loss_electricity * regional_grid_emission_factor
        )
        return transmission_loss_emission


#################################################
# 2. 有色金属行业排放计算
#################################################


class NonFerrousMetalEmissions:
    class NonFerrousGeneral:
        @staticmethod
        def calculate_fuel_burning_emission(fuel_consumption, fuel_emission_factor):
            """燃料燃烧排放量"""
            emission = fuel_consumption * fuel_emission_factor
            return emission

        @staticmethod
        def calculate_energy_as_raw_material_emission(
            reducing_agent_consumption, reducing_agent_emission_factor
        ):
            """能源作为原材料用途的排放量"""
            emission = reducing_agent_consumption * reducing_agent_emission_factor
            return emission

        @staticmethod
        def calculate_process_emission(
            raw_material_consumption, raw_material_emission_factor
        ):
            """过程排放量"""
            emission = raw_material_consumption * raw_material_emission_factor
            return emission

        @staticmethod
        def calculate_purchased_electricity_emission(
            purchased_electricity, local_electricity_emission_factor
        ):
            """企业净购入的电力消费的排放量"""
            emission = purchased_electricity * local_electricity_emission_factor
            return emission

        @staticmethod
        def calculate_purchased_heat_emission(purchased_heat, heat_emission_factor):
            """企业净购入的热力消费的排放量"""
            emission = purchased_heat * heat_emission_factor
            return emission

        @staticmethod
        def calculate_total_emission(
            fuel_burning_emission,
            energy_as_raw_material_emission,
            process_emission,
            purchased_electricity_emission,
            purchased_heat_emission,
        ):
            """汇总计算企业温室气体排放量"""
            total_emission = (
                fuel_burning_emission
                + energy_as_raw_material_emission
                + process_emission
                + purchased_electricity_emission
                + purchased_heat_emission
            )
            return total_emission

    class Aluminum:
        @staticmethod
        def calculate_fossil_fuel_emission(fuel_consumption, fuel_emission_factor):
            """燃料燃烧导致的二氧化碳排放量"""
            emission = fuel_consumption * fuel_emission_factor
            return emission

        @staticmethod
        def calculate_purchased_electricity_emission(
            purchased_electricity, electricity_emission_factor
        ):
            """电力消费产生的排放量"""
            emission = purchased_electricity * electricity_emission_factor
            return emission

        @staticmethod
        def calculate_purchased_heat_emission(purchased_heat, heat_emission_factor):
            """热力消费产生的排放量"""
            emission = purchased_heat * heat_emission_factor
            return emission


#################################################
# 3. 平板玻璃行业排放计算
#################################################


class GlassIndustryEmissions:
    @staticmethod
    def calculate_fossil_fuel_emission(
        fossil_fuel_net_consumption,
        average_low_heating_value,
        unit_heat_value_carbon_content,
        carbon_oxidation_rate,
    ):
        """化石燃料燃烧排放"""
        emission = (
            fossil_fuel_net_consumption
            * average_low_heating_value
            * unit_heat_value_carbon_content
            * carbon_oxidation_rate
        )
        return emission

    @staticmethod
    def calculate_carbon_powder_emission(
        carbon_powder_consumption, weighted_average_carbon_content
    ):
        """原料配料中碳粉氧化的排放"""
        emission = carbon_powder_consumption * weighted_average_carbon_content
        return emission

    @staticmethod
    def calculate_raw_material_decomposition_emission(
        consumed_carbonate_weight,
        carbonate_specific_emission_factor,
        carbonate_calcination_ratio,
    ):
        """原料分解产生的排放"""
        emission = (
            consumed_carbonate_weight
            * carbonate_specific_emission_factor
            * carbonate_calcination_ratio
        )
        return emission

    @staticmethod
    def calculate_purchased_power_and_heat_emission(
        purchased_electricity,
        regional_grid_emission_factor,
        purchased_heat,
        heat_emission_factor,
    ):
        """净购入使用的电力和热力对应的排放"""
        power_emission = purchased_electricity * regional_grid_emission_factor
        heat_emission = purchased_heat * heat_emission_factor
        total_emission = power_emission + heat_emission
        return total_emission


#################################################
# 4. 电子设备制造行业排放计算
#################################################


class ElectronicManufacturingEmissions:
    @staticmethod
    def calculate_electronic_manufacturing_emission(
        AD_fossil_fuel,
        EF_fossil_fuel,
        E_process,
        purchased_electricity,
        regional_grid_emission_factor,
        purchased_heat,
        heat_supply_emission_factor,
    ):
        """电子设备制造企业温室气体排放"""
        fuel_emission = sum(
            [ADi * EFi for ADi, EFi in zip(AD_fossil_fuel, EF_fossil_fuel)]
        )
        electricity_emission = purchased_electricity * regional_grid_emission_factor
        heat_emission = purchased_heat * heat_supply_emission_factor
        total_emission = (
            fuel_emission + E_process + electricity_emission + heat_emission
        )
        return total_emission


#################################################
# 5. 石油化工行业排放计算
#################################################


class PetrochemicalEmissions:
    @staticmethod
    def calculate_petrochemical_fossil_fuel_emission(
        fossil_fuel_activity_level, fossil_fuel_emission_factor
    ):
        """石油化工企业化石燃料排放"""
        emission = fossil_fuel_activity_level * fossil_fuel_emission_factor
        return emission


#################################################
# 6. 化工行业排放计算
#################################################


class ChemicalIndustryEmissions:
    @staticmethod
    def calculate_chemical_fuel_burning_emission(
        fuel_activity_level, fuel_emission_factor
    ):
        """燃料燃烧排放"""
        emission = fuel_activity_level * fuel_emission_factor
        return emission

    @staticmethod
    def calculate_chemical_process_emission(
        raw_material_activity_level, production_process_emission_factor
    ):
        """工业生产过程排放"""
        emission = raw_material_activity_level * production_process_emission_factor
        return emission

    @staticmethod
    def calculate_chemical_purchased_power_and_heat_emission(
        purchased_electricity, electricity_emission_factor
    ):
        """净购入的电力和热力导致的CO2排放量"""
        emission = purchased_electricity * electricity_emission_factor
        return emission

    @staticmethod
    def calculate_chemical_total_emission(
        fuel_burning_emission, process_emission, purchased_power_emission
    ):
        """加总计算企业温室气体排放总量"""
        total_emission = (
            fuel_burning_emission + process_emission + purchased_power_emission
        )
        return total_emission


#################################################
# 7. 矿山企业排放计算
#################################################


class MiningEmissions:
    @staticmethod
    def calculate_mining_fuel_burning_emission(
        fossil_fuel_consumption,
        fossil_fuel_carbon_content,
        fossil_fuel_carbon_oxidation_rate,
    ):
        """燃料燃烧CO2排放量"""
        emission = (
            fossil_fuel_consumption
            * fossil_fuel_carbon_content
            * fossil_fuel_carbon_oxidation_rate
            * 44
            / 12
        )
        return emission

    @staticmethod
    def calculate_carbonization_absorption_emission(
        produced_carbonized_product_weight,
        carbonized_product_carbonate_component_weight_fraction,
        carbonate_absorption_factor,
    ):
        """碳化工艺吸收的CO2量(负排放)"""
        emission = (
            produced_carbonized_product_weight
            * carbonized_product_carbonate_component_weight_fraction
            * carbonate_absorption_factor
        )
        return emission

    @staticmethod
    def calculate_carbonate_decomposition_emission(
        ore_calcination_or_roasting_amount,
        ore_calcination_or_roasting_decomposition_rate,
        ore_carbonate_component_mass_fraction,
        carbonate_emission_factor,
    ):
        """碳酸盐分解的CO2排放量"""
        emission = (
            ore_calcination_or_roasting_amount
            * ore_calcination_or_roasting_decomposition_rate
            * ore_carbonate_component_mass_fraction
            * carbonate_emission_factor
        )
        return emission

    @staticmethod
    def calculate_mining_purchased_power_and_heat_emission(
        purchased_electricity,
        electricity_emission_factor,
        purchased_heat,
        heat_emission_factor,
    ):
        """净购入电力和热力隐含的CO2排放"""
        power_emission = purchased_electricity * electricity_emission_factor
        heat_emission = purchased_heat * heat_emission_factor
        total_emission = power_emission + heat_emission
        return total_emission


#################################################
# 8. 陶瓷生产行业排放计算
#################################################


class CeramicsEmissions:
    @staticmethod
    def calculate_ceramics_fossil_fuel_emission(
        fossil_fuel_consumption, low_heating_value, co2_emission_factor
    ):
        """化石燃料燃烧排放计算"""
        emission = fossil_fuel_consumption * low_heating_value * co2_emission_factor
        return emission

    @staticmethod
    def calculate_ceramics_purchased_electricity_emission(
        purchased_electricity, regional_grid_emission_factor
    ):
        """净购入生产用电蕴含的排放计算"""
        emission = purchased_electricity * regional_grid_emission_factor
        return emission

    @staticmethod
    def calculate_ceramics_total_emission(
        fossil_fuel_emission, process_emission, purchased_electricity_emission
    ):
        """加总排放量计算"""
        total_emission = (
            fossil_fuel_emission + process_emission + purchased_electricity_emission
        )
        return total_emission


#################################################
# 9. 民用航空企业排放计算
#################################################


class CivilAviationEmissions:
    @staticmethod
    def calculate_civil_avi_emission(AD_electricity, EF_electricity, AD_heat, EF_heat):
        """民用航空企业温室气体排放"""
        emissions = (
            sum([ADi * EFi for ADi, EFi in zip(AD_electricity, EF_electricity)])
            + AD_electricity * EF_electricity
            + AD_heat * EF_heat
        )
        return emissions
