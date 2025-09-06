


from src.background_processes.background_process_base import BackgroundProcessBase


class SensorBackgroundProcess(BackgroundProcessBase):
    
    async def run_cycle(self) -> None:
        print(f"[{self.name}] polling sensors...")


